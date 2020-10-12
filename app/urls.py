from rest_framework import routers
from .views.blog_view import BlogViewSet
from .views.comment_view import CommentViewSet
from .views.auth_view import DestroyUserView
from django.conf.urls import url, include
from app.views.auth_view import TwitterLogin

router = routers.DefaultRouter()
router.register(r'api/blog', BlogViewSet)
router.register(r'api/comment', CommentViewSet)
urlpatterns = router.urls
urlpatterns += [
    url(r'auth/', include('rest_auth.urls')),
    url(r'auth/registration/', include('rest_auth.registration.urls')),
    url(r'auth/twitter/$', TwitterLogin.as_view(), name='twitter_login'),
    url(r'auth/destroy', DestroyUserView.as_view(), name="destroy")
]
