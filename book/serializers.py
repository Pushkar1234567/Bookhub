from rest_framework import serializers
from .models import BookRecommendation, Like, Comment

class BookRecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookRecommendation
        fields = ['id', 'user', 'title', 'author', 'description', 'cover_image', 'rating', 'created_at']

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'user', 'recommendation', 'created_at']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'recommendation', 'text', 'created_at']