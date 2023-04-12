from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/chat/', include('chat.urls')),
    path('api/articles/', include('articles.urls')),
    path('api/', include('users.urls')),
]
