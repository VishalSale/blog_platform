import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from django.urls import path
from blog.consumers import PostConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog_platform_assessment.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter([
        path("ws/posts/", PostConsumer.as_asgi()),
    ]),
})
