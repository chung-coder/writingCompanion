from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..models import Teacher
from ..serializers import TeacherSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    """
    Teacher Data ViewSet
    
    Permissions:
    - Teachers: can view/update their own data
    - Students: can view their teachers' data
    """
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Return teacher data based on user role"""
        user = self.request.user
        if hasattr(user, 'teacher'):
            return Teacher.objects.filter(id=user.teacher.id)
        if hasattr(user, 'student'):
            return Teacher.objects.filter(students=user.student)
        return Teacher.objects.none()