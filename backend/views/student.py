from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError, PermissionDenied
from django.contrib.auth.models import User
from ..models import Student, Class, Teacher
from ..serializers import StudentSerializer
from ..permissions import IsTeacherOrOwner, IsStudent

class StudentViewSet(viewsets.ModelViewSet):
    """
    Student Data ViewSet
    
    Permissions:
    - Teachers: view, create, update and delete their class students
    - Students: view their own data only
    """
    queryset = Student.objects.select_related('user', 'teacher', 'class_field')
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Return students based on user role (teacher/student)"""
        user = self.request.user
        if hasattr(user, 'teacher'):
            return self.queryset.filter(teacher=user.teacher)
        return self.queryset.filter(user=user)

    def check_object_permissions(self, request, obj):
        """Check permissions for viewing, updating and deleting student data"""
        super().check_object_permissions(request, obj)
        
        # For viewing (GET) operations
        if self.action == 'retrieve':
            if not ((hasattr(request.user, 'teacher') and obj.teacher == request.user.teacher) or
                   obj.user == request.user):
                raise PermissionDenied("You don't have permission to view this student")
        
        # For update (PUT/PATCH) and delete operations
        elif self.action in ['update', 'partial_update', 'destroy']:
            if not (hasattr(request.user, 'teacher') and obj.teacher == request.user.teacher):
                raise PermissionDenied("Only teachers can modify their students' information")

    def perform_create(self, serializer):
        """Create new student record (teachers only)"""
        if not hasattr(self.request.user, 'teacher'):
            raise PermissionDenied("Only teachers can create student records")
        
        serializer.save(teacher=self.request.user.teacher)

    def perform_destroy(self, instance):
        """Delete student and associated user account"""
        try:
            user = instance.user
            instance.delete()
            if user:
                user.delete()
        except Exception as e:
            raise ValidationError(f"Failed to delete student: {str(e)}")

class ListStudentInfoView(APIView):
    """
    Student Information View
    
    Endpoint for retrieving current student's detailed information:
    - Username
    - Gender
    - Email
    - Class
    - Teacher
    
    Permissions:
    - Students can only view their own information
    - Teachers can view their students' information
    """
    permission_classes = (IsAuthenticated, IsStudent)

    def get(self, request, *args, **kwargs):
        try:
            # Get student with all related data in a single query
            student = Student.objects.select_related(
                'user',
                'teacher',
                'class_field'
            ).filter(user=request.user).first()

            if not student:
                return Response(
                    {'error': 'Student record not found'},
                    status=status.HTTP_404_NOT_FOUND
                )
            
            # Return student's information
            return Response({
                "user_name": student.name,
                "gender": "Male" if student.gender == "M" else "Female",
                "email": student.user.email,
                "class_name": student.class_field.class_name if student.class_field else None,
                "teacher_name": student.teacher.name if student.teacher else None
            })

        except Exception as e:
            return Response(
                {'error': f'Failed to retrieve student information: {str(e)}'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
