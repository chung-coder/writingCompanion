from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# 認證相關
from backend.views.auth import (
    MyObtainTokenPairView,
    RegisterView,
    ChangePasswordView,
    UpdateProfileView,
    LogoutView
)

# 日記相關
from backend.views.diary import (
    DiaryViewSet,
    ListWeeklyDiaryView
)

# GPT 相關
from backend.views.genAI import (
    GptinteractionViewSet,
    GptassistanceViewSet,
    GptInteractionView,
    GptAssistanceView
)

# 學生相關
from backend.views.student import (
    ListStudentInfoView,
    StudentViewSet
)

# 班級相關
from backend.views.class_management import ClassViewSet

# 教師相關
from backend.views.teacher import TeacherViewSet

# 統計相關
from backend.views.statistics import (
    WordCountStatistics,
    CountInteractionView,
    ListFavoriteDiaryView
)

router = routers.DefaultRouter()
router.register(r"students", StudentViewSet)
router.register(r"teachers", TeacherViewSet)
router.register(r"classes", ClassViewSet)
router.register(r"diaries", DiaryViewSet)
router.register(r"gpt-assistance", GptassistanceViewSet)
router.register(r"gpt-interaction", GptinteractionViewSet)

urlpatterns = [
    # Admin
    path("admin/", admin.site.urls),
    
    # API 根路徑
    path("api/", include(router.urls)),
    
    # 認證相關
    path("api/login/", MyObtainTokenPairView.as_view(), name="token_obtain_pair"),
    path("api/login/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/logout/", LogoutView.as_view(), name="logout"),
    path("api/register/", RegisterView.as_view(), name="auth_register"),
    path("api/change-password/", ChangePasswordView.as_view(), name="auth_change_password"),
    path("api/update-profile/", UpdateProfileView.as_view(), name="auth_update_profile"),
    
    # 學生相關
    path("api/student-info/", ListStudentInfoView.as_view(), name="student_info"),
    
    # 日記相關
    path("api/weekly-diaries/", ListWeeklyDiaryView.as_view(), name="weekly_diaries"),
    path("api/favorite-diaries/", ListFavoriteDiaryView.as_view(), name="favorite_diaries"),
    
    # GPT 相關
    path("api/gpt/interact/", GptInteractionView, name="gpt_interaction"),
    path("api/gpt/assist/", GptAssistanceView, name="gpt_assistance"),
    
    # 統計相關
    path("api/statistics/word-count/", WordCountStatistics.as_view(), name="word_count_statistics"),
    path("api/statistics/interaction/", CountInteractionView.as_view(), name="interaction_statistics"),
]
