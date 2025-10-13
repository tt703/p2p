import json
import logging
import random
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.db.models import Q
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django import forms
from django.db import IntegrityError
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

from .models import User, Chat, Message, Student, TutoringSession

logger = logging.getLogger(__name__)

def index(request):
    tutors = User.objects.filter(is_tutor=True).order_by('-performance_rating')
    students = Student.objects.select_related('user').all()
    return render(request, 'index.html', {'tutors': tutors, 'students': students})
def tutors(request):
    return render(request, 'tutors.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


@csrf_exempt
@login_required
def save_tutoring_session(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        date = data.get('date')
        description = data.get('description')
        student_id = data.get('student')

        if not student_id:
            return JsonResponse({'success': False, 'error': 'Student ID is required'})

        try:
            student = Student.objects.get(id=student_id)
            tutoring_session = TutoringSession.objects.create(
                tutor=request.user,
                student=student,
                description=description,
                date=date
            )
            return JsonResponse({'success': True})
        except Student.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Student not found'})

    return JsonResponse({'success': False, 'error': 'Invalid request method'})




@login_required
def tutor_students(request):
    tutor = request.user

    students = Student.objects.filter(tutoring_sessions__tutor=tutor).select_related('user').distinct()

    sessions = TutoringSession.objects.filter(tutor=tutor).select_related('student')

    upcoming_sessions = sessions.filter(date__gte=timezone.now()).order_by('date')

    student_data = [{'id': student.id, 'username': student.user.username} for student in students]
    session_data = [{
        'date': session.date,
        'description': session.description,
        'student': {'username': session.student.user.username}
    } for session in upcoming_sessions]

    return JsonResponse({
        'students': student_data,
        'sessions': session_data,
    })


from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.db import IntegrityError
from django.urls import reverse
from .models import User, Student

import logging

logger = logging.getLogger(__name__)


def register(request):
    if request.method == "POST":
        logger.info("POST request received for registration")

        # Get form data
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirmation = request.POST.get("confirmation")

        # Password confirmation check
        if password != confirmation:
            logger.warning("Passwords do not match.")
            return render(request, "register.html", {
                "message": "Passwords must match."
            })

        # Become tutor and additional fields
        become_tutor = request.POST.get("become_tutor") in ["true", "on"]
        subject = request.POST.get("subject") if become_tutor else None
        mark = request.POST.get("mark") if become_tutor else None

        # Ensure mark is valid for tutor registration
        is_tutor = become_tutor and mark and int(mark) >= 80

        # Attempt to create a new user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.is_tutor = is_tutor
        user.subject = subject if is_tutor else None
        user.save()

        # Create a student profile if not a tutor
        if not is_tutor:
            Student.objects.create(user=user, subject=None, is_online=True)

        # Log the user in and redirect
        login(request, user)
        logger.info("User created and logged in successfully.")
        return redirect(reverse("index"))

    logger.info("Rendering registration form.")
    return render(request, "register.html")


@login_required
def student_list(request):
    students = Student.objects.select_related('user').all()
    return render(request, 'students/student_list.html', {'students': students})



def tutor_list(request):
    subject_filter = request.GET.get('subject', None)
    tutors = User.objects.filter(is_tutor=True)

    if subject_filter:
        tutors = tutors.filter(subject=subject_filter)

    tutors = tutors.order_by('-performance_rating')

    return render(request, 'tutors/tutor_list.html', {'tutors': tutors})

@login_required
def chat_list(request):

    user_chats = Chat.objects.filter(
        participants=request.user,
        messages__isnull=False
    ).distinct().prefetch_related('participants', 'messages')


    chats = []
    for chat in user_chats:
        other_user = chat.participants.exclude(id=request.user.id).first()
        if other_user:
            chats.append({
                'id': chat.id,
                'username': other_user.username,
                'is_online': other_user.student.is_online if hasattr(other_user, 'student') else False,
            })

    return render(request, 'chats.html', {
        'tutors': User.objects.filter(is_tutor=True).order_by('-performance_rating'),
        'students': Student.objects.select_related('user').all(),
        'chats': chats
    })




@login_required
def chat_messages(request, chat_id):
    chat = get_object_or_404(Chat, id=chat_id, participants=request.user)
    messages = chat.messages.order_by('timestamp').values('sender_id', 'content')

    data = {
        'chat_with': chat.participants.exclude(id=request.user.id).first().username,
        'messages': [
            {
                'content': message['content'],
                'is_sent': message['sender_id'] == request.user.id
            }
            for message in messages
        ]
    }
    return JsonResponse(data)


@csrf_exempt
@login_required
def send_message(request, chat_id):
    if request.method == 'POST':
        chat = get_object_or_404(Chat, id=chat_id, participants=request.user)
        data = json.loads(request.body)

        content = data.get('content')
        if content:
            message = Message.objects.create(
                chat=chat,
                sender=request.user,
                content=content
            )
            return JsonResponse({'success': True, 'message_id': message.id})
        else:
            return JsonResponse({'error': 'Message content required'}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)


@login_required
def student_dashboard(request):
    student = get_object_or_404(Student, user=request.user)
    subjects = set()


    user_chats = Chat.objects.filter(participants=request.user)

    for chat in user_chats:
        other_user = chat.participants.exclude(id=request.user.id).first()
        if other_user and other_user.is_tutor:

            if other_user.subject:
                subjects.add(other_user.subject)

    return render(request, 'students/student_dashboard.html', {
        'subjects': list(subjects)
    })
@login_required
def chat_detail(request, chat_id):
    chat = get_object_or_404(Chat, id=chat_id)
    messages = chat.messages.all()
    context = {
        'chat': chat,
        'messages': messages,
        'chat_with': chat.participants.exclude(id=request.user.id).first(),
    }
    return render(request, 'chat_detail.html', context)

@login_required
def chat_with_user(request, username):
    tutor = get_object_or_404(User, username=username)

    chat = Chat.objects.filter(participants=request.user).filter(participants=tutor).first()
    if not chat:
        chat = Chat.objects.create()
        chat.participants.add(request.user, tutor)

    return redirect('chat_detail', chat_id=chat.id)

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }
