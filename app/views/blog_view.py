from rest_framework import viewsets
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import MethodNotAllowed

from ..models.blog import Blog
from .serializer.blog_serializer import BlogReadSerializer, BlogPostSerializer, BlogSearchFilter
from rest_framework.response import Response
from .permission_class import BlogPermission


class BlogViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (BlogPermission,)
    queryset = Blog.objects.all()
    serializer_class = BlogReadSerializer
    filter_class = BlogSearchFilter

    def get_serializer_class(self):
        if self.request.method == "POST":
            return BlogPostSerializer
        return self.serializer_class

    def create(self, request, *args, **kwargs):
        data = request.data
        data["author"] = request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, pk):
        if not Blog.objects.is_own_blog(user_id=request.user.id, blog_id=pk):
            raise MethodNotAllowed("Update blog")
        return super().update(request, pk)

    def partial_update(self, request, pk):
        if not Blog.objects.is_own_blog(user_id=request.user.id, blog_id=pk):
            raise MethodNotAllowed("Update blog")
        return super().partial_update(request, pk)

    def destroy(self, request, pk):
        if not Blog.objects.is_own_blog(user_id=request.user.id, blog_id=pk):
            raise MethodNotAllowed("Delete blog")
        return super().destroy(request, pk)
