from django.urls import path
from .views import MessagesList, CreateMessage

urlpatterns = [
    path('messages/', MessagesList.as_view()),
    path('create/', CreateMessage.as_view()),
]
