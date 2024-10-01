from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import action, api_view
from .models import Post, Category, Tag, Comment, Like
from .serializers import PostSerializer, CategorySerializer, TagSerializer, CommentSerializer, LikeSerializer


# API Overview
@api_view(['GET'])
def apiOverview(request):
    blog_urls = {
        'Posts': {
            'List': '/posts/',
            'Detail': '/posts/<str:pk>/',
            'Create': '/posts/create/',
            'Update': '/posts/update/<str:pk>/',
            'Delete': '/posts/delete/<str:pk>/',
        },
        'Categories': {
            'List': '/categories/',
            'Detail': '/categories/<str:pk>/',
            'Create': '/categories/create/',
            'Update': '/categories/update/<str:pk>/',
            'Delete': '/categories/delete/<str:pk>/',
        },
        'Tags': {
            'List': '/tags/',
            'Detail': '/tags/<str:pk>/',
            'Create': '/tags/create/',
            'Update': '/tags/update/<str:pk>/',
            'Delete': '/tags/delete/<str:pk>/',
        },
        'Comments': {
            'List': '/comments/',
            'Detail': '/comments/<str:pk>/',
            'Create': '/comments/create/',
            'Update': '/comments/update/<str:pk>/',
            'Delete': '/comments/delete/<str:pk>/',
        },
        'Likes': {
            'List': '/likes/',
            'Detail': '/likes/<str:pk>/',
            'Create': '/likes/create/',
            'Delete': '/likes/delete/<str:pk>/',
        },
    }
    return Response(blog_urls)


# Post Views

@api_view(['GET'])
def postList(request):
    post = Post.objects.all()
    serializer = PostSerializer(post, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def postDetail(request, pk):
    post = Post.objects.get(id = pk)
    serializer = PostSerializer(post, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createPost(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(author=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'PATCH'])
def updatePost(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = PostSerializer(post, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def deletePost(request, pk):
    post = Post.objects.get(id = pk)
    post.delete()
    return Response('Post is Successfully delete')
    

# Category Views


@api_view(['GET'])
def categoryList(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def categoryDetail(request, pk):
    category = Category.objects.get(id=pk)
    serializer = CategorySerializer(category, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createCategory(request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def updateCategory(request, pk):
    category = Category.objects.get(id=pk)
    serializer = CategorySerializer(instance=category, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteCategory(request, pk):
    category = Category.objects.get(id=pk)
    category.delete()
    return Response("Category successfully deleted!")


# Tag Views


@api_view(['GET'])
def tagList(request):
    tags = Tag.objects.all()
    serializer = TagSerializer(tags, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def tagDetail(request, pk):
    tag = Tag.objects.get(id=pk)
    serializer = TagSerializer(tag, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createTag(request):
    serializer = TagSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def updateTag(request, pk):
    tag = Tag.objects.get(id=pk)
    serializer = TagSerializer(instance=tag, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteTag(request, pk):
    tag = Tag.objects.get(id=pk)
    tag.delete()
    return Response("Tag successfully deleted!")



# Comment Views


@api_view(['GET'])
def commentList(request):
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def commentDetail(request, pk):
    comment = Comment.objects.get(id=pk)
    serializer = CommentSerializer(comment, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createComment(request):
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)  
    return Response(serializer.data)

@api_view(['PUT'])
def updateComment(request, pk):
    comment = Comment.objects.get(id=pk)
    serializer = CommentSerializer(instance=comment, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteComment(request, pk):
    comment = Comment.objects.get(id=pk)
    comment.delete()
    return Response("Comment successfully deleted!")


# Like Views


@api_view(['GET'])
def likeList(request):
    likes = Like.objects.all()
    serializer = LikeSerializer(likes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def likeDetail(request, pk):
    like = Like.objects.get(id=pk)
    serializer = LikeSerializer(like, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createLike(request):
    serializer = LikeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteLike(request, pk):
    like = Like.objects.get(id=pk)
    like.delete()
    return Response("Like successfully deleted!")



# user viewset

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
