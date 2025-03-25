from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# Authentication related
from backend.views.auth import (
    MyObtainTokenPairView,
    RegisterView,
    ChangePasswordView,
    UpdateProfileView,
    LogoutView
)

# Diary related
from backend.views.diary import (
    DiaryViewSet,
    ListWeeklyDiaryView
)

# GPT related
from backend.views.genAI import (
    InteractionViewSet,
    AssistanceViewSet,
    InteractionView,
    AssistanceView
)

# Student related
from backend.views.student import (
    ListStudentInfoView,
    StudentViewSet
)

# Class related
from backend.views.class_management import ClassViewSet

# Teacher related
from backend.views.teacher import TeacherViewSet

# Statistics related
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
router.register(r"gpt-assistance", AssistanceViewSet)
router.register(r"gpt-interaction", InteractionViewSet)

urlpatterns = [
    # Admin
    path("admin/", admin.site.urls),
    
    # API root path
    path("api/", include(router.urls)),
    
    # Authentication related
    path("api/login/", MyObtainTokenPairView.as_view(), name="token_obtain_pair"),
    path("api/login/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/logout/", LogoutView.as_view(), name="logout"),
    path("api/register/", RegisterView.as_view(), name="auth_register"),
    path("api/change-password/", ChangePasswordView.as_view(), name="auth_change_password"),
    path("api/update-profile/", UpdateProfileView.as_view(), name="auth_update_profile"),
    
    # Student related
    path("api/student-info/", ListStudentInfoView.as_view(), name="student_info"),
    
    # Diary related
    path("api/weekly-diaries/", ListWeeklyDiaryView.as_view(), name="weekly_diaries"),
    path("api/favorite-diaries/", ListFavoriteDiaryView.as_view(), name="favorite_diaries"),
    
    # GPT related
    path("api/gpt/interact/", InteractionView.as_view(), name="gpt_interaction"),
    path("api/gpt/assist/", AssistanceView.as_view(), name="gpt_assistance"),
    
    # Statistics related
    path("api/statistics/word-count/", WordCountStatistics.as_view(), name="word_count_statistics"),
    path("api/statistics/interaction/", CountInteractionView.as_view(), name="interaction_statistics"),
]
