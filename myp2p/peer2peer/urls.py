from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tutors/', views.tutors, name='tutors'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('chats/', views.chat_list, name='chats'),
    path('student/', views.student_dashboard, name='student_dashboard'),
    path('tutor_students/', views.tutor_students, name='tutor_students'),
    path('save_tutoring_session/', views.save_tutoring_session, name='save_tutoring_session'),
    path('chat/<int:chat_id>/messages/', views.chat_messages, name='chat_messages'),
    path('chat/<int:chat_id>/send/', views.send_message, name='send_message'),
    path('students/', views.student_list, name='student_list'),
    path('chat/<int:chat_id>/', views.chat_detail, name='chat_detail'),
    path('chat/<str:username>/', views.chat_with_user, name='chat_with_user'),
    path('chat/<int:chat_id>/send/', views.send_message, name='send_message'),


]
