from django.urls import path
from chatroom import views

app_name = "chatroom"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("<str:room_name>/", views.chatroom, name="chat-room"),
]
