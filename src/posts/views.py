from django.shortcuts import render

# rest-framework
from rest_framework import viewsets, status
# custom imports
from rest_framework.response import Response

from .models import Post, User, Like
from src.posts.serializer import PostSerializer, UserSerializer, LikeSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def list(self, request, *args, **kwargs):
        self.queryset = self.queryset.filter(user=request.user.id)
        context = super(PostViewSet, self).list(request, *args, **kwargs)
        # context, update({"count": self.queryset.count()})

        return context

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def list(self, request, *args, **kwargs):
        self.queryset = self.queryset.filter(user=request.user.id)
        serializer = self.get_serializer(self.queryset, many=True)
        msg = "list of likes"
        if not request.user.is_superuser:
            count = self.queryset.count()
        else:
            msg = "is admin"
            count = 100

        return Response({
            'data': serializer.data,
            'msg': msg,
            'count': count
        })

