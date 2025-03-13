from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
from ..serializers import (
    MyTokenObtainPairSerializer,
    RegisterSerializer,
    ChangePasswordSerializer,
    UpdateUserSerializer,
)

class AuthBaseView:
    """認證相關視圖的基礎類"""
    
    @staticmethod
    def get_error_response(message, status_code=status.HTTP_400_BAD_REQUEST):
        return Response(
            {'error': message},
            status=status_code
        )

class MyObtainTokenPairView(TokenObtainPairView):
    """
    登入視圖
    
    返回 JWT token pair (access token 和 refresh token)
    """
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer

class RegisterView(AuthBaseView, generics.CreateAPIView):
    """
    註冊視圖
    
    允許新用戶註冊，需提供：
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
                'message': '註冊成功',
                'user_id': user.id,
                'username': user.username,
                'email': user.email
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return self.get_error_response(f'註冊失敗: {str(e)}')

class UpdateProfileView(AuthBaseView, generics.UpdateAPIView):
    """
    更新用戶資料視圖
    
    允許已登入用戶更新其個人資料：
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
                'message': '資料更新成功',
                'username': user.username,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name
            })
        except Exception as e:
            return self.get_error_response(f'更新失敗: {str(e)}')

class ChangePasswordView(AuthBaseView, generics.UpdateAPIView):
    """
    更改密碼視圖
    
    允許已登入用戶更改密碼，需提供：
    - old_password
    - password (新密碼)
    - password2 (確認新密碼)
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
                'message': '密碼更改成功'
            })
        except Exception as e:
            return self.get_error_response(f'密碼更改失敗: {str(e)}')