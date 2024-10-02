from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('postlist/', views.postList, name="postlist"),
    path('postdetail/<str:pk>/', views.postDetail, name="postdetail"),
    path('createpost/', views.createPost, name="createpost"),
    path('updatepost/<str:pk>/', views.updatePost, name="updatepost"),
    path('deletepost/<str:pk>/', views.deletePost, name="deletepost"),
    path('categories/', views.categoryList, name="category-list"),
    path('categories/<str:pk>/', views.categoryDetail, name="category-detail"),
    path('tags/', views.tagList, name="tag-list"),
    path('tags/<str:pk>/', views.tagDetail, name="tag-detail"),
    path('likes/', views.likeList, name="like-list"),
    path('likes/<str:pk>/', views.likeDetail, name="like-detail"),
]
