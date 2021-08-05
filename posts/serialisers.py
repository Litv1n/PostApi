from rest_framework.serializers import ModelSerializer

from .models import Post

# создаем сериалайзер для нашей модели Post
class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'body']