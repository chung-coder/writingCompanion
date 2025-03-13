from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..models import Teacher
from ..serializers import TeacherSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    """
    教師資料的 ViewSet
    
    提供教師資料的 CRUD 操作
    """
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """根據用戶權限返回教師資料"""
        if self.request.user.is_staff:
            return Teacher.objects.all()
        return Teacher.objects.filter(
            student__user=self.request.user
        ).distinct()