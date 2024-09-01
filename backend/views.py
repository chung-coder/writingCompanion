from rest_framework import permissions, viewsets, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from django.http import HttpResponse, JsonResponse

from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Count, Case, When, IntegerField
from django.contrib.auth.models import User

from .serializers import (
    MyTokenObtainPairSerializer,
    RegisterSerializer,
    ChangePasswordSerializer,
    UpdateUserSerializer,
)

from backend.models import Class, Diary, Gptassistance, Gptinteraction, Student, Teacher
from backend.serializers import (
    ClassSerializer,
    DiarySerializer,
    GptinteractionSerializer,
    GptassistanceSerializer,
    StudentSerializer,
    TeacherSerializer,
)

import openai
import json
from django.conf import settings

# Create your views here.
openai.api_key = settings.OPENAI_API_KEY


@csrf_exempt
def GptInteractioneView(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            title = data.get("title")
            date = data.get("date")
            mood = data.get("mood")
            target = data.get("target")
            diary_content = data.get("diary_content")
            user_messages = data.get("messages")
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

    MODEL = "gpt-4o"
    system_content = """
    你只用繁體中文回覆我的問題，並請將回答的內容控制在 200 字以內。你是一位擁有豐富寫作經驗且熱於助人的寫作教練，我是國小三年級的學生，請根據你的專業來協助我撰寫日常札記，我們採用一問一答的方式進行互動。

    規範
    語言：只用繁體中文回覆我的問題
    回答長度：請將每次回答的內容控制在 200 字以內，但在產出日記和 JSON 格式時不限字數。
    回覆方式：不要直接撰寫日記，而是引導使用者思考問題並提供提示。

    表現風格
    風格：像一位擁有豐富寫作經驗且熱於助人的寫作教練。
    建議方式：當使用者完成撰寫時，像一位心理專家或好朋友給予建議。

    步驟
    1. 使用者會告知今天日期以及當天的心情，並提及日記的讀者（自己、朋友、同學或家人）。
    2. 根據使用者提供的資訊，詢問今天過得如何，討論日記內容與方向。
    3. 根據使用者回應，選擇適當步驟進行互動。

    互動步驟
    A. 繼續討論日記內容，等待使用者回應。
    B. 日記內容完整後，檢查句子邏輯與錯字，提供修正版本，等待使用者回應。
    C. 解答使用者對修正版本的疑問，提供討論後的版本。
    D. 確認使用者滿意修正版本。
    E. 根據日記內容給予鼓勵、安慰、分析或建議，等待使用者回應。
    F. 確認使用者滿意日記後，提供日記的原始完整版本。
    G. 詢問使用者對原始版本的滿意度，是否需要參考修正版本。
    H. 詢問使用者是否有修改或補充想法，協助進行調整。
    I. 完成日記後，輸出成 JSON 格式，每一輪對話包含以下欄位：
    "Role"：角色（"User" 或 "Assistant"）
    "Content"：內容（對話文字）
    "Counter"：對話次數
    """
    user_content = (
        "關於我的日記，標題是「"
        + title
        + "」，撰寫日期是「"
        + date
        + "」，我今天的心情「"
        + mood
        + "」，且這篇日記是紀錄給「"
        + target
        + "」，目前撰寫的作文內容：\n"
        + diary_content
    )

    if user_messages is None:
        response = openai.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": system_content},
                {
                    "role": "user",
                    "content": user_content,
                },
            ],
        )
    else:
        gpt_messages = [{"role": "system", "content": system_content}]
        for message in user_messages:
            gpt_messages.append(message)
        response = openai.chat.completions.create(
            model=MODEL,
            messages=gpt_messages,
        )
    return HttpResponse(response.choices[0].message.content)


@csrf_exempt
def GptAssistanceView(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            title = data.get("title")
            date = data.get("date")
            mood = data.get("mood")
            target = data.get("target")
            diary_content = data.get("diary_content")
            problem = data.get("problem")
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

    MODEL = "gpt-4o"
    system_content = """
    你是一位擁有豐富寫作經驗且熱於助人的寫作教練，
    我是國小三年級的學生，現在正在撰寫一篇日記，
    然而，我目前撰寫日記遇到了一些困難，請根據你的專業來協助我撰寫日記，
    但不需要提供改寫的日記版本，同時，你只能用繁體中文回覆我的問題。
    """

    user_content = (
        "關於我的日記，標題是「"
        + title
        + "」，撰寫日期是「"
        + date
        + "」，我今天的心情「"
        + mood
        + "」，且這篇日記是紀錄給「"
        + target
        + "」，目前撰寫的作文內容：\n"
        + diary_content
        + "這是我目前遇到的問題：\n"
        + problem
    )

    response = openai.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_content},
            {
                "role": "user",
                "content": user_content,
            },
        ],
    )

    print(response.choices[0].message.content)
    return HttpResponse(response.choices[0].message.content)


class ListStudentInfoView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        user_id = self.request.user.id
        student_info = Student.objects.filter(user_id=user_id).values()[0]
        gender = "男" if student_info["gender"] == "M" else "女"
        email = User.objects.filter(pk=user_id).values()[0]["email"]
        class_name = Class.objects.filter(id=student_info["class_field_id"]).values()[
            0
        ]["class_name"]
        teacher_name = Teacher.objects.filter(id=student_info["teacher_id"]).values()[
            0
        ]["name"]

        return Response(
            {
                "user_name": student_info["name"],
                "gender": gender,
                "email": email,
                "class_name": class_name,
                "teacher_name": teacher_name,
            }
        )


class ListFavoriteDiaryView(generics.ListAPIView):
    serializer_class = DiarySerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user_id = self.request.user.id
        student_id = Student.objects.filter(user_id=user_id).values()[0]["id"]

        return Diary.objects.filter(student_id=student_id).filter(is_favorite=True)


class CountInteractionView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        user_id = request.user.id
        student_id = Student.objects.filter(user_id=user_id).values()[0]["id"]
        interaction_diary_counter = (
            Diary.objects.filter(student_id=student_id)
            .filter(diary_type="Interaction")
            .count()
        )
        assistance_diary_counter = (
            Diary.objects.filter(student_id=student_id)
            .filter(diary_type="Assistance")
            .count()
        )
        totol_diary = interaction_diary_counter + assistance_diary_counter
        target_counts = Diary.objects.filter(student_id=student_id).aggregate(
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

        mood_counts = Diary.objects.filter(student_id=student_id).aggregate(
            very_good=Count(
                Case(When(mood="很好", then=1), output_field=IntegerField())
            ),
            good=Count(Case(When(mood="好", then=1), output_field=IntegerField())),
            normal=Count(Case(When(mood="普通", then=1), output_field=IntegerField())),
            bad=Count(Case(When(mood="差", then=1), output_field=IntegerField())),
            very_bad=Count(
                Case(When(mood="很差", then=1), output_field=IntegerField())
            ),
        )
        return Response(
            {
                "interaction_diary_counter": interaction_diary_counter,
                "assistance_diary_counter": assistance_diary_counter,
                "total": totol_diary,
                "target_counts": target_counts,
                "mood": mood_counts,
            }
        )


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


class UpdateProfileView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UpdateUserSerializer


class ChangePasswordView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class ClassViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    permission_classes = [permissions.IsAuthenticated]


class DiaryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Diary.objects.all()
    serializer_class = DiarySerializer
    permission_classes = [permissions.IsAuthenticated]


class GptinteractionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Gptinteraction.objects.all()
    serializer_class = GptinteractionSerializer
    permission_classes = [permissions.IsAuthenticated]


class GptassistanceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Gptassistance.objects.all()
    serializer_class = GptassistanceSerializer
    permission_classes = [permissions.IsAuthenticated]


class StudentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]


class TeacherViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [permissions.IsAuthenticated]
