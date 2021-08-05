from rest_framework.viewsets import ModelViewSet

from .models import Post
from .serialisers import PostSerializer

# создаем информационное представление для Vue
class PostsViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
