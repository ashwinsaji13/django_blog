from django.conf.urls import include
from django.urls import path

# rest-framework
from rest_framework.routers import DefaultRouter

# custom imports
from .views import PostViewSet, UserViewSet, LikeViewSet

router = DefaultRouter()
router.register('like', LikeViewSet, base_name='likes')
router.register('posts', PostViewSet, base_name='posts')
router.register('users', UserViewSet, base_name='users')

urlpatterns = [
    path('api/', include(router.urls)),
]
