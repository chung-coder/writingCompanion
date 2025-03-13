from rest_framework import viewsets, generics, permissions
from rest_framework.permissions import IsAuthenticated
from ..models import Diary, Student
from ..serializers import DiarySerializer


class DiaryViewSet(viewsets.ModelViewSet):
    queryset = Diary.objects.all()
    serializer_class = DiarySerializer
    permission_classes = [permissions.IsAuthenticated]

class ListWeeklyDiaryView(generics.ListAPIView):
    serializer_class = DiarySerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user_id = self.request.user.id
        student_id = Student.objects.filter(user_id=user_id).values()[0]["id"]
        start = self.request.query_params.get("start_date")
        end = self.request.query_params.get("end_date")
        
        return Diary.objects.filter(student_id=student_id).filter(
            date__range=[start, end]
        )