from django.contrib import admin
from chatroom.models import ChatRoomMessageModel


@admin.register(ChatRoomMessageModel)
class NoteModelAdmin(admin.ModelAdmin):
    pass
