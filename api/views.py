from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import *




class TagAPIView(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class CategoryAPIView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class TopicAPIView(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class NewsAPIView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = NewsSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


