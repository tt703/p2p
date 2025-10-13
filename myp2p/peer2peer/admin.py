from django.contrib import admin
from peer2peer.models import User, Student, TutoringSession, Chat, Message

admin.site.register(User)
admin.site.register(Student)
admin.site.register(TutoringSession)
admin.site.register(Message)
admin.site.register(Chat)
