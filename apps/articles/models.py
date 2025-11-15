from django.db import models

from apps.users.models import User


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    tags = models.JSONField(default=list)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    analysis = models.JSONField(default=dict, blank=True)

    def __str__(self):
        return f"<Article: {self.title}>"
