from rest_framework import serializers
from .models import Articles


class ArticleSerializer:
    class Meta:
        model = Articles
        fields = "__all__"
