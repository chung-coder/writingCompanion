from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from ..serializers import (
    MyTokenObtainPairSerializer,
    RegisterSerializer,
    ChangePasswordSerializer,
    UpdateUserSerializer,
)

class AuthBaseView:
    """Base class for authentication related views"""
    
    @staticmethod
    def get_error_response(message, status_code=status.HTTP_400_BAD_REQUEST):
        return Response(
            {'error': message},
            status=status_code
        )

class MyObtainTokenPairView(TokenObtainPairView):
    """
    Login View
    
    Returns JWT token pair (access token and refresh token)
    """
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer

class RegisterView(AuthBaseView, generics.CreateAPIView):
    """
    Registration View
    
    Allows new users to register with:
    - username
    - password
    - email
    - first_name
    - last_name
    """
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return self.get_error_response(serializer.errors)
        
        try:
            user = serializer.save()
            return Response({
                'message': 'Registration successful',
                'user_id': user.id,
                'username': user.username,
                'email': user.email
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return self.get_error_response(f'Registration failed: {str(e)}')

class UpdateProfileView(AuthBaseView, generics.UpdateAPIView):
    """
    Update Profile View
    
    Allows authenticated users to update their profile:
    - username
    - email
    - first_name
    - last_name
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = UpdateUserSerializer

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        
        if not serializer.is_valid():
            return self.get_error_response(serializer.errors)
        
        try:
            user = serializer.save()
            return Response({
                'message': 'Profile updated successfully',
                'username': user.username,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name
            })
        except Exception as e:
            return self.get_error_response(f'Update failed: {str(e)}')

class ChangePasswordView(AuthBaseView, generics.UpdateAPIView):
    """
    Change Password View
    
    Allows authenticated users to change their password by providing:
    - old_password
    - password (new password)
    - password2 (confirm new password)
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        
        if not serializer.is_valid():
            return self.get_error_response(serializer.errors)
        
        try:
            serializer.save()
            return Response({
                'message': 'Password changed successfully'
            })
        except Exception as e:
            return self.get_error_response(f'Password change failed: {str(e)}')

class LogoutView(AuthBaseView, generics.GenericAPIView):
    """
    Logout View
    
    Allows authenticated users to logout by blacklisting their refresh token.
    Requires:
    - refresh token in request body
    """
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh")
            if not refresh_token:
                return self.get_error_response("Refresh token is required")
                
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({
                "message": "Logged out successfully"
            })
        except Exception as e:
            return self.get_error_response(f"Logout failed: {str(e)}")