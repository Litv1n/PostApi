from rest_framework.viewsets import ModelViewSet

from .models import Post
from .serialisers import PostSerializer

# Create View Set Of Posts
class PostsViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
