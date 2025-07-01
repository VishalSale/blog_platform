from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, AuthorViewSet

router = DefaultRouter()
router.register(r'authors', AuthorViewSet, basename='author')
router.register(r'posts', PostViewSet, basename='post')

urlpatterns = [
    path('', include(router.urls)),
]
