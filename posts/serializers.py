
from rest_framework import serializers

from posts.models import Posts, HashTags


class PostSerializer(serializers.ModelSerializer):
    class Meta():
        model = Posts
        fields = '__all__'


class HashTagSerializer(serializers.ModelSerializer):
    class Meta():
        model = HashTags
        fields = '__all__'

