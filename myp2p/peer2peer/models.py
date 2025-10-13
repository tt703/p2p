from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
class User(AbstractUser):
    is_tutor = models.BooleanField(default=False)
    subject = models.CharField(max_length=50, blank=True, null=True)
    performance_rating = models.FloatField(default=0.0)
    is_online = models.BooleanField(default=True)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100, blank=True, null=True)
    is_online = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username


class TutoringSession(models.Model):
    tutor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tutoring_sessions')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='tutoring_sessions')
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return f"{self.tutor.username} with {self.student.user.username} on {self.date}"


class Chat(models.Model):
    participants = models.ManyToManyField(User)

class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')  # Correctly reference chat
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender}: {self.content}'
