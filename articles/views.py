from rest_framework import permissions, generics
from .models import Articles
from .serializers import ArticleSerializer


class ArticlesListView(generics.ListAPIView):
    serializer_class = ArticleSerializer
    queryset = Articles.objects.all()
