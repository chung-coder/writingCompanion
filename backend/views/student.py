from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from ..models import Student, Class, Teacher
from ..serializers import StudentSerializer

class StudentBaseView:
    """學生相關視圖的基礎類"""
    
    @staticmethod
    def get_error_response(message, status_code=status.HTTP_400_BAD_REQUEST):
        return Response(
            {'error': message},
            status=status_code
        )

class ListStudentInfoView(APIView):
    """
    學生資訊視圖
    
    返回當前登入學生的詳細資訊，包括：
    - 用戶名稱
    - 性別
    - 電子郵件
    - 班級
    - 教師
    """
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        try:
            # 獲取學生資訊
            student_info = Student.objects.filter(
                user_id=request.user.id
            ).values().first()
            
            if not student_info:
                return Response(
                    {'error': '找不到學生資料'},
                    status=status.HTTP_404_NOT_FOUND
                )

            # 獲取用戶郵件
            email = User.objects.filter(
                pk=request.user.id
            ).values_list('email', flat=True).first()

            # 獲取班級名稱
            class_name = Class.objects.filter(
                id=student_info["class_field_id"]
            ).values_list('class_name', flat=True).first()

            # 獲取教師名稱
            teacher_name = Teacher.objects.filter(
                id=student_info["teacher_id"]
            ).values_list('name', flat=True).first()

            return Response({
                "user_name": student_info["name"],
                "gender": "男" if student_info["gender"] == "M" else "女",
                "email": email,
                "class_name": class_name,
                "teacher_name": teacher_name
            })

        except Exception as e:
            return Response(
                {'error': f'獲取學生資訊失敗: {str(e)}'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class StudentViewSet(viewsets.ModelViewSet):
    """
    學生資料的 ViewSet
    
    提供學生資料的 CRUD 操作
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """只返回當前用戶的資料"""
        if self.request.user.is_staff:
            return Student.objects.all()
        return Student.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """創建時自動關聯當前用戶"""
        serializer.save(user=self.request.user)