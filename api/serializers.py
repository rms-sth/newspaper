from rest_framework import serializers
from newsapp.models import *




#Better to use ModelSerializer => works for all model
class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'url', 'word', 'created_at')


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'url', 'name')


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ('id', 'url', 'subject', 'category', 'starter')


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'url', 'title', 'content', 'image', 'topic', 'tag', 'post_count', 'created_at','status', 'author', 'update_by')
