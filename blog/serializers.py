from rest_framework import serializers
from .models import Author, Post

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'email']

class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)

    # This field is for output, so it uses the AuthorSerializer to show author details
    author_id = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all(), write_only=True, required=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created_at', 'author', 'author_id']

    def create(self, validated_data):
        author = validated_data.pop('author_id')
        validated_data['author'] = author
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if 'author_id' in validated_data:
            author = validated_data.pop('author_id')
            validated_data['author'] = author
        return super().update(instance, validated_data)
