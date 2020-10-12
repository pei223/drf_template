from django.contrib.auth import get_user_model
from django.db import models
from .blog import Blog


class CommentQuerySet(models.QuerySet):
    def blog_comments(self, blog_id):
        return self.filter(blog_id=blog_id)


class Comment(models.Model):
    blog_id = models.ForeignKey(Blog, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    comment = models.TextField(max_length=10000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CommentQuerySet.as_manager()
