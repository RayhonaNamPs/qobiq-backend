from rest_framework import serializers
from .models import ChatRoom, Message
from users.serializers import AccountsSerializer

class ChatRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRoom
        fields = ('id', 'name')

class MessageSerializer(serializers.ModelSerializer):
    sender = AccountsSerializer()
    chat_room = ChatRoomSerializer()

    class Meta:
        model = Message
        field = ('id', 'sender', 'chat_room', 'content', 'timestamp')