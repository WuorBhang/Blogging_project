from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import User
from .serializers import RegisterSerializer, LoginSerializer, ProfileSerializer

class RegisterView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user_data = serializer.save()
            return Response({
                "user": {
                    "username": user_data['user'].username,
                    "email": user_data['user'].email,
                },
                "token": user_data['token']
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]  
    lookup_field = 'username'

    def delete(self, request, *args, **kwargs):
        user = self.get_object()  # Get the user to delete
        user.delete()  # Delete the user
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProfileDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        # Return the logged-in user's profile
        return self.request.user

