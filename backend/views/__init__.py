# 認證相關視圖
from .auth import (
    MyObtainTokenPairView,
    RegisterView,
    ChangePasswordView,
    UpdateProfileView
)

# 日記相關視圖
from .diary import (
    DiaryViewSet,
    ListWeeklyDiaryView
)

# GPT 相關視圖
from .genAI import (
    GptinteractionViewSet,
    GptassistanceViewSet,
    GptInteractionView,
    GptAssistanceView
)

# 學生相關視圖
from .student import (
    ListStudentInfoView,
    StudentViewSet
)

# 班級相關視圖
from .class_management import ClassViewSet

# 教師相關視圖
from .teacher import TeacherViewSet

# 統計相關視圖
from .statistics import (
    WordCountStatistics,
    CountInteractionView,
    ListFavoriteDiaryView
)

__all__ = [
    # 認證相關
    'MyObtainTokenPairView',
    'RegisterView',
    'ChangePasswordView',
    'UpdateProfileView',
    
    # 日記相關
    'DiaryViewSet',
    'ListWeeklyDiaryView',
    'ListFavoriteDiaryView',
    
    # GPT 相關
    'GptinteractionViewSet',
    'GptassistanceViewSet',
    'gpt_interaction_view',
    'gpt_assistance_view',
    
    # 學生相關
    'ListStudentInfoView',
    'StudentViewSet',
    
    # 班級相關
    'ClassViewSet',
    
    # 教師相關
    'TeacherViewSet',
    
    # 統計相關
    'WordCountStatistics',
    'CountInteractionView'
]