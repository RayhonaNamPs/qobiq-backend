from django.db import models


class Articles(models.Model):
    content = models.TextField()
    title = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
