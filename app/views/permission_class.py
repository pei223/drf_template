from enum import Enum

from django.http import QueryDict
from rest_framework import permissions
from ..models.blog import Blog


class ViewAction(Enum):
    CREATE = "create"
    LIST = "list"
    DESTROY = "destroy"
    UPDATE = "update"
    PARTIAL_UPDATE = "partial_update"


class BlogPermission(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        if view.action == ViewAction.LIST.value:
            return True
        return super(BlogPermission, self).has_permission(request, view)


class CommentPermission(permissions.IsAdminUser):
    def has_permission(self, request, view):
        if view.action in [ViewAction.CREATE.value, ViewAction.LIST.value]:
            return True
        return super(CommentPermission, self).has_permission(request, view)
