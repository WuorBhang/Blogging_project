from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post, Category, Tag, Comment, Like

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    category = CategorySerializer()
    tags = TagSerializer(many=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'category', 'tags', 'date_created', 'published_date']

    def create(self, validated_data):
        # Extract category and tags data
        category_data = validated_data.pop('category')
        tags_data = validated_data.pop('tags')
        category, created = Category.objects.get_or_create(**category_data)
        post = Post.objects.create(category=category, **validated_data)
        for tag_data in tags_data:
            tag, created = Tag.objects.get_or_create(**tag_data)
            post.tags.add(tag)

        return post
    
    def update(self, instance, validated_data):
        category_data = validated_data.pop('category', None)
        if category_data:
            category, created = Category.objects.get_or_create(**category_data)
            instance.category = category
        tags_data = validated_data.pop('tags', None)
        if tags_data:
            tags = []
            for tag_data in tags_data:
                tag, created = Tag.objects.get_or_create(**tag_data)
                tags.append(tag)
            instance.tags.set(tags) 
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.published_date = validated_data.get('published_date', instance.published_date)

        instance.save()
        return instance

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Comment
        fields = ['id', 'user', 'post', 'content', 'parent', 'date_created']


class LikeSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Like
        fields = ['id', 'user', 'post', 'date_liked']