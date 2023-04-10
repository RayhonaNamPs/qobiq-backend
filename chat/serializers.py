from rest_framework import serializers
from .models import Message
from users.serializers import AccountsSerializer


class CreateMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'chat_room', 'content', 'timestamp')


class MessageSerializer(serializers.ModelSerializer):
    sender = AccountsSerializer()

    class Meta:
        model = Message
        fields = '__all__'
