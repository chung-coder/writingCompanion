from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, generics
from django.db.models import Count, Case, When, IntegerField, Sum
from ..permissions import IsStudent
from datetime import datetime
from ..models import Student, Diary
from ..serializers import DiarySerializer

class WordCountStatistics(APIView):
    """
    Word Count Statistics View
    
    Returns total word count statistics for each month of the specified year
    """
    permission_classes = (IsAuthenticated, IsStudent)

    def get(self, request, *args, **kwargs):
        try:
            # Get year from query parameters, default to current year
            year = request.query_params.get("year", datetime.now().year)
            
            # Query word count statistics for each month of the year
            word_count_data = (
                Diary.objects.filter(
                    student=request.user.student,
                    date__year=year
                )
                .values("date__month")
                .annotate(total_word_count=Sum("word_count"))
                .order_by("date__month")
            )

            # Convert to dictionary format
            result = {
                month["date__month"]: month["total_word_count"] 
                for month in word_count_data
            }

            # Fill in missing months with zero values
            for month in range(1, 13):
                if month not in result:
                    result[month] = 0

            return Response({
                "year": year,
                "word_count_statistics": result
            })

        except Exception as e:
            return Response(
                {'error': f'Failed to get word count statistics: {str(e)}'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class CountInteractionView(APIView):
    """
    Interaction Statistics View
    
    Returns:
    1. Number of interaction diaries
    2. Number of assistance diaries
    3. Total number of diaries
    4. Target reader statistics
    5. Mood statistics
    """
    permission_classes = (IsAuthenticated, IsStudent)

    def get(self, request, *args, **kwargs):
        try:
            # Get base queryset using user.student
            student_diaries = Diary.objects.filter(student=request.user.student)

            # Calculate counts for different diary types
            interaction_count = student_diaries.filter(
                diary_type="Interaction"
            ).count()
            assistance_count = student_diaries.filter(
                diary_type="Assistance"
            ).count()
            total_count = interaction_count + assistance_count

            # Calculate target reader distribution
            target_counts = student_diaries.aggregate(
                self_count=Count(
                    Case(When(target="自己", then=1), output_field=IntegerField())
                ),
                friend_count=Count(
                    Case(When(target="朋友", then=1), output_field=IntegerField())
                ),
                family_count=Count(
                    Case(When(target="家人", then=1), output_field=IntegerField())
                ),
                other_count=Count(
                    Case(When(target="其他", then=1), output_field=IntegerField())
                ),
            )

            # Calculate mood distribution
            mood_counts = student_diaries.aggregate(
                very_good=Count(
                    Case(When(mood="很好", then=1), output_field=IntegerField())
                ),
                good=Count(
                    Case(When(mood="好", then=1), output_field=IntegerField())
                ),
                normal=Count(
                    Case(When(mood="普通", then=1), output_field=IntegerField())
                ),
                bad=Count(
                    Case(When(mood="差", then=1), output_field=IntegerField())
                ),
                very_bad=Count(
                    Case(When(mood="很差", then=1), output_field=IntegerField())
                ),
            )

            return Response({
                "interaction_diary_counter": interaction_count,
                "assistance_diary_counter": assistance_count,
                "total": total_count,
                "target_counts": target_counts,
                "mood": mood_counts,
            })

        except Exception as e:
            return Response(
                {'error': f'Failed to get interaction statistics: {str(e)}'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class ListFavoriteDiaryView(generics.ListAPIView):
    """
    Favorite Diary List View
    
    Returns all diaries favorited by the current user
    """
    serializer_class = DiarySerializer
    permission_classes = (IsAuthenticated, IsStudent)

    def get_queryset(self):
        """Get user's favorite diary list"""
        return Diary.objects.filter(
            student=self.request.user.student,
            is_favorite=True
        ).order_by('-date')  # Sort by date in descending order
    
    def list(self, request, *args, **kwargs):
        """Override list method to add error handling"""
        try:
            queryset = self.get_queryset()
            if not queryset.exists():
                return Response(
                    {'message': 'No favorite diaries found'},
                    status=status.HTTP_200_OK
                )
            
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
            
        except Exception as e:
            return Response(
                {'error': f'Failed to get favorite diaries: {str(e)}'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )