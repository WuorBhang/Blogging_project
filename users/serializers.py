from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth.password_validation import validate_password
from django.utils.translation import gettext_lazy as _
from .models import User, Profile


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role']


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password_confirm = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password_confirm']
    
    def validate(self, data):
        # Check if both passwords match
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return data

    def create(self, validated_data):
        # Create a new user with the validated data
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        # Generate and return a token for the new user
        token = Token.objects.create(user=user)
        return {'user': user, 'token': token.key}



class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True)

    def validate(self, data):
        # Extract username and password from the request data
        username = data.get('username')
        password = data.get('password')

        # Authenticate the user
        user = authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError(_('Invalid login credentials.'))

        # Check if the user is active
        if not user.is_active:
            raise serializers.ValidationError(_('User account is disabled.'))

        # Get or create the token for the authenticated user
        token, created = Token.objects.get_or_create(user=user)
        
        # Return the validated data, including the token and user details
        return {
            'token': token.key,
            'user': {
                'username': user.username,
                'email': user.email,
            }
        }



class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')

    class Meta:
        model = Profile
        fields = ['username', 'bio', 'role', 'profile_picture']