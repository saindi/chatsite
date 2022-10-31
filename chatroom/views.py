from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.views.generic import TemplateView

from chatroom.models import ChatRoomMessageModel


class HomeView(TemplateView):
    template_name = 'home.html'


def chatroom(request: HttpRequest, room_name: str) -> HttpResponse:

    ctx = {
        "room_name": room_name,
        "object_list": ChatRoomMessageModel.objects.filter(group_name=room_name),
    }

    return render(request, "chatroom.html", ctx)
