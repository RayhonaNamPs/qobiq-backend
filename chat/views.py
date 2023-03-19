from django.shortcuts import get_object_or_404
from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from .models import ChatRoom, Message
from .serializers import ChatRoomSerializer, MessageSerializer


class ChatRoomListCreateView(generics.ListCreateAPIView):
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer


class JoinChatRoomView(generics.GenericAPIView):
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer

    def post(self, request, *args, **kwargs):
        chat_room = self.get_object()
        user = request.user
        chat_room.users.add(user)
        chat_room.save()
        return Response(status=status.HTTP_200_OK)


class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer

    def get_queryset(self):
        chat_room = get_object_or_404(ChatRoom, id=self.kwargs['chat_room_id'])
        return chat_room.messages.all()

    def perform_create(self, serializer):
        chat_room = get_object_or_404(ChatRoom, id=self.kwargs['chat_room_id'])
        serializer.save(sender=self.request.user, chat_room=chat_room)
