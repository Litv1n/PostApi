from django.urls import path

from rest_framework import routers

from .views import PostsViewSet

router = routers.DefaultRouter()
router.register('posts', PostsViewSet)

urlpatterns = router.urls