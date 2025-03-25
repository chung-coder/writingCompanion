# Authentication related views
from .auth import (
    MyObtainTokenPairView,
    RegisterView,
    ChangePasswordView,
    UpdateProfileView
)

# Diary related views
from .diary import (
    DiaryViewSet,
    ListWeeklyDiaryView
)

# GPT related views
from .genAI import (
    InteractionViewSet,
    AssistanceViewSet,
    InteractionView,
    AssistanceView
)

# Student related views
from .student import (
    ListStudentInfoView,
    StudentViewSet
)

# Class related views
from .class_management import ClassViewSet

# Teacher related views
from .teacher import TeacherViewSet

# Statistics related views
from .statistics import (
    WordCountStatistics,
    CountInteractionView,
    ListFavoriteDiaryView
)

__all__ = [
    # Authentication related
    'MyObtainTokenPairView',
    'RegisterView',
    'ChangePasswordView',
    'UpdateProfileView',
    
    # Diary related
    'DiaryViewSet',
    'ListWeeklyDiaryView',
    'ListFavoriteDiaryView',
    
    # GPT related
    'GptinteractionViewSet',
    'GptassistanceViewSet',
    'gpt_interaction_view',
    'gpt_assistance_view',
    
    # Student related
    'ListStudentInfoView',
    'StudentViewSet',
    
    # Class related
    'ClassViewSet',
    
    # Teacher related
    'TeacherViewSet',
    
    # Statistics related
    'WordCountStatistics',
    'CountInteractionView'
]