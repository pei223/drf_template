from rest_framework import serializers
from ...models.comment import Comment
from django_filters import rest_framework as filters


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'blog_id', 'name', 'comment', 'created_at', 'updated_at')


class CommentSearchFilter(filters.FilterSet):
    class Meta:
        model = Comment
        fields = {
            "blog_id": ["exact"],
        }
