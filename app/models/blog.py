from django.contrib.auth import get_user_model
from django.db import models


class BlogQuerySet(models.QuerySet):
    def title_list(self, user_id):
        return self.filter(author=user_id).values("title")

    def is_own_blog(self, blog_id: int, user_id: int):
        blog = self.filter(id=blog_id).values()
        if blog is None or len(blog) == 0:
            return False
        return blog[0]["author_id"] == user_id


class Blog(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, primary_key=False)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, default="", max_length=50000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = BlogQuerySet.as_manager()
