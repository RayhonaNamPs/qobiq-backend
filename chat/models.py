from django.db import models
from users.models import Accounts


class Message(models.Model):
    content = models.TextField()
    sender = models.ForeignKey(Accounts, on_delete=models.CASCADE, related_name='messages')
    chat_room = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender.fullname}: {self.content[:50]}'
