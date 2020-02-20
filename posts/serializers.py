from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.HyperlinkedRelatedField(
        view_name='user-detail', read_only=True)
    username = serializers.ReadOnlyField(source='owner.username') 
    class Meta:
        model = Post
        fields = ('url', 'id', 'created_at', 'title', 'description', 'loc_lat', 'loc_long', 'reward','owner','username')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.HyperlinkedRelatedField(
        many=True,view_name='post-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'email', 'first_name', 'last_name', 'posts')