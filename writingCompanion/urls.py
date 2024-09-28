from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from backend import views

router = routers.DefaultRouter()
router.register(r"students", views.StudentViewSet)
router.register(r"teachers", views.TeacherViewSet)
router.register(r"class", views.ClassViewSet)
router.register(r"diary", views.DiaryViewSet)
router.register(r"gpt-assistance", views.GptassistanceViewSet)
router.register(r"gpt-interaction", views.GptinteractionViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("login/", views.MyObtainTokenPairView.as_view(), name="token_obtain_pair"),
    path("login/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("register/", views.RegisterView.as_view(), name="auth_register"),
    path(
        "api/change_password/",
        views.ChangePasswordView.as_view(),
        name="auth_change_password",
    ),
    path(
        "api/update_profile/",
        views.UpdateProfileView.as_view(),
        name="auth_update_profile",
    ),
    path("api/weekly_diary/", views.ListWeeklyDiaryView.as_view(), name="list_diary"),
    path(
        "api/count_diaryType/",
        views.CountInteractionView.as_view(),
        name="count_interaction",
    ),
    path(
        "api/favorite_diary/",
        views.ListFavoriteDiaryView.as_view(),
        name="favorite_diary",
    ),
    path(
        "api/student_info/",
        views.ListStudentInfoView.as_view(),
        name="get_student_info",
    ),
    path(
        "api/word-count-statistics/",
        views.WordCountStatistics.as_view(),
        name="word-count-statistics",
    ),
    path("api/assistance/", views.GptAssistanceView, name="gpt_assistance"),
    path("api/interaction/", views.GptInteractioneView, name="gpt_interaction"),
]
