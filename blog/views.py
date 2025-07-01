from django.shortcuts import render
from rest_framework import viewsets, filters
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.utils.dateparse import parse_date
from .models import Post, Author
from .serializers import PostSerializer, AuthorSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['author__name', 'created_at']

    # Broadcast WebSocket notification
    def perform_create(self, serializer):
        post = serializer.save()
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "posts_updates",
            {
                "type": "send_new_post",
                "message": f"New post created: {post.title} by {post.author.name}",
            }
        )
    
    # filter by date
    def get_queryset(self):
        queryset = super().get_queryset()
        date_str = self.request.query_params.get('date')
        if date_str:
            date = parse_date(date_str)
            if date:
                queryset = queryset.filter(created_at__date=date)
        return queryset
    