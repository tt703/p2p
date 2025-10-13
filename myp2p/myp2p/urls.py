
from django.contrib import admin
from django.urls import path, include
#from

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('peer2peer.urls')),
    #path("chat/<str:chat_box_name>/"),chat_box, name="chat"),

]

