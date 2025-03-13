from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, generics
from django.db.models import Count, Case, When, IntegerField, Sum
from django.contrib.auth.models import User
from datetime import datetime
from ..models import Student, Diary
from ..serializers import DiarySerializer

class StatisticsBaseView(APIView):
    """統計相關視圖的基礎類"""
    permission_classes = (IsAuthenticated,)

    def get_student_id(self):
        """獲取當前用戶對應的學生ID"""
        try:
            return Student.objects.filter(
                user_id=self.request.user.id
            ).values_list('id', flat=True)[0]
        except IndexError:
            return None

    def handle_no_student_error(self):
        """處理找不到學生資料的錯誤"""
        return Response(
            {'error': '找不到學生資料'},
            status=status.HTTP_404_NOT_FOUND
        )

class WordCountStatistics(StatisticsBaseView):
    """
    字數統計視圖
    
    返回指定年份每月的總字數統計
    """
    def get(self, request, *args, **kwargs):
        student_id = self.get_student_id()
        if not student_id:
            return self.handle_no_student_error()

        try:
            # 獲取查詢參數中的年份，默認為當前年份
            year = request.query_params.get("year", datetime.now().year)
            
            # 查詢該年度每月的字數統計
            word_count_data = (
                Diary.objects.filter(
                    student_id=student_id,
                    date__year=year
                )
                .values("date__month")
                .annotate(total_word_count=Sum("word_count"))
                .order_by("date__month")
            )

            # 轉換為字典格式
            result = {
                month["date__month"]: month["total_word_count"] 
                for month in word_count_data
            }

            # 補充缺失的月份數據
            for month in range(1, 13):
                if month not in result:
                    result[month] = 0

            return Response({
                "year": year,
                "word_count_statistics": result
            })

        except Exception as e:
            return Response(
                {'error': f'獲取字數統計失敗: {str(e)}'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class CountInteractionView(StatisticsBaseView):
    """
    互動統計視圖
    
    返回：
    1. 互動日記數量
    2. 協助日記數量
    3. 總日記數量
    4. 目標讀者統計
    5. 心情統計
    """
    def get(self, request, *args, **kwargs):
        student_id = self.get_student_id()
        if not student_id:
            return self.handle_no_student_error()

        try:
            # 獲取基本查詢集
            student_diaries = Diary.objects.filter(student_id=student_id)

            # 計算不同類型的日記數量
            interaction_count = student_diaries.filter(
                diary_type="Interaction"
            ).count()
            assistance_count = student_diaries.filter(
                diary_type="Assistance"
            ).count()
            total_count = interaction_count + assistance_count

            # 統計目標讀者分布
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

            # 統計心情分布
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
                {'error': f'獲取統計資料失敗: {str(e)}'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class ListFavoriteDiaryView(generics.ListAPIView):
    """
    收藏日記列表視圖
    
    返回當前用戶收藏的所有日記
    """
    serializer_class = DiarySerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """
        獲取用戶收藏的日記清單
        
        Returns:
            QuerySet: 收藏的日記查詢集
        
        Raises:
            Http404: 當找不到學生資料時
        """
        try:
            student_id = Student.objects.filter(
                user_id=self.request.user.id
            ).values_list('id', flat=True)[0]
            
            return Diary.objects.filter(
                student_id=student_id,
                is_favorite=True
            ).order_by('-date')  # 按日期降序排序
            
        except IndexError:
            return Diary.objects.none()  # 返回空查詢集
    
    def list(self, request, *args, **kwargs):
        """
        重寫list方法以添加錯誤處理
        """
        try:
            queryset = self.get_queryset()
            if not queryset.exists():
                return Response(
                    {'message': '沒有找到收藏的日記'},
                    status=status.HTTP_200_OK
                )
            
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
            
        except Exception as e:
            return Response(
                {'error': f'獲取收藏日記失敗: {str(e)}'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )