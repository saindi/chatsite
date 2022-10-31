from django.db import models


class ChatRoomMessageModel(models.Model):
    class Meta:
        db_table = "message"
        verbose_name = "message"
        verbose_name_plural = "messages"

    create_at = models.DateTimeField(auto_now_add=True)
    group_name = models.CharField(max_length=32)
    message = models.TextField()

    def __repr__(self):
        return(f"<ChatRoomMessageModel("
               f"create_at={self.create_at}, "
               f"group_name={self.group_name}, "
               f"message={self.message}, "
               f")>")

    def __str__(self):
        return self.message
