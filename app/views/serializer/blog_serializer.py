from rest_framework import serializers
from ...models.blog import Blog
from .user_serializer import UserSerializer
from django_filters import rest_framework as filters


class BlogReadSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Blog
        fields = ('id', 'author', 'title', 'description', 'created_at', 'updated_at')


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('author', 'title', 'description',)


class BlogSearchFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr="contains", field_name="title")

    class Meta:
        model = Blog
        fields = {
            "id": ["exact", ],
            "title": ["contains", ],
            "author": ["exact", ]
        }
