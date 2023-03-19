from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'chatrooms/(?P<chat_room_id>\d+)/messages', views.MessageViewSet, basename='messages')

urlpatterns = [
    path('api/chatrooms/', views.ChatRoomListCreateView.as_view(), name='chatroom-list-create'),
    path('api/chatrooms/<int:pk>/join/', views.JoinChatRoomView.as_view(), name='chatroom-join'),
    path('api/', include(router.urls)),
]
