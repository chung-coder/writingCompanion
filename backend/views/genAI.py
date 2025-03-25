from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.conf import settings
from ..models import Gptinteraction, Gptassistance
from ..serializers import GptinteractionSerializer, GptassistanceSerializer
from ..permissions import IsStudent
import openai
import json
from datetime import datetime

openai.api_key = settings.OPENAI_API_KEY

class GPTConfig:
    """GPT Configuration and Utility Class"""
    
    MODEL = "gpt-4"
    
    INTERACTION_SYSTEM_CONTENT = """
    你只用繁體中文回覆我的問題，並請將回答的內容控制在 200 字以內。你是一位擁有豐富寫作經驗且熱於助人的寫作教練，
    我是國小三年級的學生，請根據你的專業來協助我撰寫日常札記，我們採用一問一答的方式進行互動。

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
    """

    ASSISTANCE_SYSTEM_CONTENT = """
    你是一位擁有豐富寫作經驗且熱於助人的寫作教練，
    我是國小三年級的學生，現在正在撰寫一篇日記，
    然而，我目前撰寫日記遇到了一些困難，請根據你的專業來協助我撰寫日記，
    但不需要提供改寫的日記版本，同時，你只能用繁體中文回覆我的問題。
    """

    @staticmethod
    def validate_request_data(data):
        """Validate required fields in request data"""
        required_fields = ['title', 'date', 'mood', 'target', 'diary_content']
        missing_fields = [field for field in required_fields if not data.get(field)]
        
        if missing_fields:
            return f'Missing required fields: {", ".join(missing_fields)}'
        return None

    @staticmethod
    def format_diary_content(data):
        """Format diary content for GPT input"""
        return (
            f"關於我的日記，標題是「{data.get('title')}」，"
            f"撰寫日期是「{data.get('date')}」，"
            f"我今天的心情「{data.get('mood')}」，"
            f"且這篇日記是紀錄給「{data.get('target')}」，"
            f"目前撰寫的作文內容：\n{data.get('diary_content')}"
        )

class BaseGPTView(APIView):
    """Base class for GPT-related views"""
    
    permission_classes = [IsAuthenticated, IsStudent]
    
    def handle_gpt_request(self, messages):
        """Handle GPT API request with error handling"""
        try:
            response = openai.chat.completions.create(
                model=GPTConfig.MODEL,
                messages=messages
            )
            return response.choices[0].message.content
        except openai.APIError as e:
            raise Exception(f'OpenAI API error: {str(e)}')

    def validate_and_process_request(self, request):
        """Validate request data and prepare for processing"""
        try:
            data = request.data
            error = GPTConfig.validate_request_data(data)
            if error:
                return Response({'error': error}, status=status.HTTP_400_BAD_REQUEST)
            return data
        except Exception as e:
            return Response(
                {'error': f'Invalid request data: {str(e)}'},
                status=status.HTTP_400_BAD_REQUEST
            )

class InteractionView(BaseGPTView):
    """View for handling writing interaction with GPT"""

    def post(self, request):
        data = self.validate_and_process_request(request)
        if isinstance(data, Response):
            return data

        try:
            # Prepare messages for GPT
            messages = [
                {"role": "system", "content": GPTConfig.INTERACTION_SYSTEM_CONTENT}
            ]

            if data.get('messages'):
                messages.extend(data['messages'])
            else:
                messages.append({
                    "role": "user",
                    "content": GPTConfig.format_diary_content(data)
                })

            # Get GPT response
            gpt_response = self.handle_gpt_request(messages)

            # Save interaction record
            Gptinteraction.objects.create(
                user=request.user,
                diary_id=data.get('diary_id'),
                interaction_time=data.get('date', datetime.now()),
                dialogue_record=json.dumps(messages + [
                    {'role': 'assistant', 'content': gpt_response}
                ])
            )

            return Response({'response': gpt_response})

        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class AssistanceView(BaseGPTView):
    """View for handling writing assistance with GPT"""

    def post(self, request):
        data = self.validate_and_process_request(request)
        if isinstance(data, Response):
            return data

        try:
            if not data.get('problem'):
                return Response(
                    {'error': 'Missing problem description'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            # Prepare content for GPT
            user_content = (
                f"{GPTConfig.format_diary_content(data)}\n"
                f"這是我目前遇到的問題：\n{data['problem']}"
            )

            # Get GPT response
            messages = [
                {'role': 'system', 'content': GPTConfig.ASSISTANCE_SYSTEM_CONTENT},
                {'role': 'user', 'content': user_content}
            ]
            gpt_response = self.handle_gpt_request(messages)

            # Save assistance record
            Gptassistance.objects.create(
                user=request.user,
                diary_id=data.get('diary_id'),
                interaction_time=data.get('date', datetime.now()),
                user_input=data['problem'],
                gpt_response=gpt_response
            )

            return Response({'response': gpt_response})

        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class InteractionViewSet(viewsets.ModelViewSet):
    """ViewSet for managing GPT interaction records"""
    
    serializer_class = GptinteractionSerializer
    permission_classes = [IsAuthenticated, IsStudent]
    queryset = Gptinteraction.objects.all()

    def get_queryset(self):
        """Return interactions for current student"""
        return Gptinteraction.objects.filter(
            student=self.request.user.student
        ).order_by('-interaction_time')

class AssistanceViewSet(viewsets.ModelViewSet):
    """ViewSet for managing GPT assistance records"""
    
    serializer_class = GptassistanceSerializer
    permission_classes = [IsAuthenticated, IsStudent]
    queryset = Gptassistance.objects.all()

    def get_queryset(self):
        """Return assistance records for current student"""
        return Gptassistance.objects.filter(
            student=self.request.user.student
        ).order_by('-interaction_time')