from django.urls import path
from .views import RegisterView, LoginView, ProfileDetailView, UserDeleteView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileDetailView.as_view(), name='profile'),
    path('deleteuser/<str:username>/', UserDeleteView.as_view(), name='deleteuser'),
]
