from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..models import Class, Student
from ..serializers import ClassSerializer

class ClassViewSet(viewsets.ModelViewSet):
    """
    Class Data ViewSet
    
    Basic CRUD operations for class data:
    - List all classes (teacher) or own class (student)
    - Get class details
    - Create class (teacher only)
    - Update class (teacher only)
    - Delete class (teacher only)
    """
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Return class data based on user permissions"""
        # Teachers can see all classes
        if hasattr(self.request.user, 'teacher'):
            return Class.objects.all()
        
        # Students can only see their own class
        student = Student.objects.get(user=self.request.user)
        return Class.objects.filter(id=student.class_field_id)
