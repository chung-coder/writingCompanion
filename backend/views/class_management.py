from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..models import Class
from ..serializers import ClassSerializer

class ClassViewSet(viewsets.ModelViewSet):
    """
    班級資料的 ViewSet
    
    提供班級資料的 CRUD 操作
    """
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """根據用戶權限返回班級資料"""
        if self.request.user.is_staff:
            return Class.objects.all()
        return Class.objects.filter(
            student__user=self.request.user
        ).distinct()