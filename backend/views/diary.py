from rest_framework import viewsets, generics, permissions, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from datetime import datetime
from ..models import Diary, Student
from ..serializers import DiarySerializer
from ..permissions import IsTeacherOrOwner
from rest_framework.exceptions import PermissionDenied
from django.core.exceptions import ValidationError
import re

class DiaryViewSet(viewsets.ModelViewSet):
    """
    Diary Data ViewSet
    
    Basic CRUD operations for diary entries:
    - List all diaries
    - Get diary details
    - Create diary (student only)
    - Update diary (student only)
    - Delete diary (student only)
    """
    queryset = Diary.objects.all()  # Default queryset, will be filtered in get_queryset
    serializer_class = DiarySerializer
    permission_classes = [permissions.IsAuthenticated, IsTeacherOrOwner]

    def get_queryset(self):
        """
        Return diary entries based on user permissions.
        
        Returns:
            QuerySet: Filtered diary entries based on user role
        """
        user = self.request.user
        try:
            if hasattr(user, 'teacher'):
                return Diary.objects.filter(student__teacher=user.teacher)
            elif hasattr(user, 'student'):
                return Diary.objects.filter(student__user=user)
            else:
                return Diary.objects.none()
        except Exception as e:
            raise ValidationError(f"Failed to retrieve diaries: {str(e)}")

    def perform_create(self, serializer):
        """
        Automatically set the student when creating a diary.
        Calculate and save the word count of the diary content.
        
        This method is called by the CreateModelMixin when saving the diary instance.
        It ensures that the diary is associated with the currently authenticated student.
        
        Raises:
            PermissionDenied: If the user is not a student
            ValidationError: If there are issues with the student association
        """
        user = self.request.user
        if not hasattr(user, 'student'):
            raise PermissionDenied("User is not associated with a student profile")
            
        try:
            # Get the diary data
            diary_data = serializer.validated_data
            content = diary_data.get('content', '')
            
            # Define a regular expression pattern for Chinese characters and punctuation
            chinese_pattern = r'[\u4e00-\u9fff\u3000-\u303F\uff00-\uffef.,!?]'

            # Use re.findall to find all Chinese characters and punctuation in the text
            chinese_elements = re.findall(chinese_pattern, content)

            # Return the count of Chinese characters and punctuation
            word_count = len(chinese_elements)
            
            # Add word count to the data
            diary_data['word_count'] = word_count
            
            # Save the diary with word count
            serializer.save(student=user.student, **diary_data)
        except ValidationError as e:
            raise ValidationError(f"Failed to create diary: {str(e)}")

class ListWeeklyDiaryView(generics.ListAPIView):
    """
    Weekly Diary Data View
    
    Endpoint for retrieving diary entries within a date range:
    - Requires start_date and end_date (YYYY-MM-DD format)
    - Returns sorted diary entries for the specified period
    """
    serializer_class = DiarySerializer
    permission_classes = (IsAuthenticated, IsTeacherOrOwner)

    def get_queryset(self):
        """Return diary entries for the specified date range"""
        try:
            # Get and validate date parameters
            start = self.request.query_params.get("start_date")
            end = self.request.query_params.get("end_date")
            
            if not start or not end:
                raise ValueError("Both start_date and end_date are required")
            
            # Validate date format
            try:
                start_date = datetime.strptime(start, '%Y-%m-%d').date()
                end_date = datetime.strptime(end, '%Y-%m-%d').date()
            except ValueError:
                raise ValueError("Invalid date format. Use YYYY-MM-DD")

            if start_date > end_date:
                raise ValueError("start_date cannot be later than end_date")

            # Get student's diary entries
            student_id = self.request.user.student.id
            return Diary.objects.filter(
                student_id=student_id,
                date__range=[start_date, end_date]
            ).order_by('date')
            
        except Student.DoesNotExist:
            return Diary.objects.none()
        except ValueError as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )