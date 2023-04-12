from rest_framework import generics,  permissions
from .models import Message
from .serializers import MessageSerializer, CreateMessageSerializer


class MessagesList(generics.ListAPIView):
    serializer_class = MessageSerializer

    def get_queryset(self):
        chat_room = self.request.query_params.get('chat_room')
        queryset = Message.objects.filter(chat_room=chat_room)
        return queryset


class CreateMessage(generics.CreateAPIView):
    serializer_class = CreateMessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)
