from django.db import models
from users.models import Accounts

class ChatRoom(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Message(models.Model):
    content = models.TextField()
    sender = models.ForeignKey(Accounts, on_delete=models.CASCADE, related_name='messages')
    chat_room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name='messages')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender.first_name}: {self.content[:50]}'
