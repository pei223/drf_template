from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import MethodNotAllowed

from ..models.comment import Comment
from .serializer.comment_serializer import CommentSerializer, CommentSearchFilter
from rest_framework import permissions
from .permission_class import CommentPermission


class CommentViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (CommentPermission,)
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_class = CommentSearchFilter

    def list(self, request, *args, **kwargs):
        search_blog_id = request.GET.get("blog_id")
        if search_blog_id is None:
            raise MethodNotAllowed("List comment")
        return super().list(request, *args, **kwargs)
