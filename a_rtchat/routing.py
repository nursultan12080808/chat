from django.urls import path
from .consumers import *

websocet_urlpatterns = [
    path("ws/chatroom/<str:chatroom_name>", ChatroomConsumer.as_asgi()),
]