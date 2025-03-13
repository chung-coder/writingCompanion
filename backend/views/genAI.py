from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from ..models import Gptinteraction, Gptassistance
from ..serializers import GptinteractionSerializer, GptassistanceSerializer
import openai
import json

openai.api_key = settings.OPENAI_API_KEY

class GPTConfig:
    MODEL = "gpt-4o"

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
    def create_user_content(title, date, mood, target, diary_content):
        return (
            f"關於我的日記，標題是「{title}」，"
            f"撰寫日期是「{date}」，"
            f"我今天的心情「{mood}」，"
            f"且這篇日記是紀錄給「{target}」，"
            f"目前撰寫的作文內容：\n{diary_content}"
        )
    
    @staticmethod
    def validate_request_data(title, date, mood, target, diary_content):
        required_fields = {
            'title': title,
            'date': date,
            'mood': mood,
            'target': target,
            'diary_content': diary_content
        }
    
        missing_fields = [field for field, value in required_fields.items() if not value]
        
        if missing_fields:
            return JsonResponse({
                'error': f'Missing required fields: {", ".join(missing_fields)}'
            }, status=400)
        return None


class GptinteractionViewSet(viewsets.ModelViewSet):
    """
    GPT Interaction ViewSet
    """
    queryset = Gptinteraction.objects.all()
    serializer_class = GptinteractionSerializer
    permission_classes = [permissions.IsAuthenticated]


class GptassistanceViewSet(viewsets.ModelViewSet):
    """
    GPT Assistance ViewSet
    """
    queryset = Gptassistance.objects.all()
    serializer_class = GptassistanceSerializer
    permission_classes = [permissions.IsAuthenticated]


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def GptInteractionView(request):
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    validation_error = GPTConfig.validate_request_data(data)

    if validation_error:
        return validation_error

    try:
        messages = [{"role": "system", "content": GPTConfig.INTERACTION_SYSTEM_CONTENT}]

        user_content = GPTConfig.create_user_content(data)
        if data.get('messages'):
            messages.extend(data['messages'])
        else:
            messages.append({"role": "user", "content": user_content})

        response = openai.chat.completions.create(
            model=MODEL,
            messages=gpt_messages,
        )
        
        Gptinteraction.objects.create(
            user=request.user,
            diary_id=data.get('diary_id'),
            interaction_time=data.get('date'),
            dialogue_record=json.dumps(messages + [{'role': 'assistant', 'content': response.choices[0].message.content}])
        )

        return Response({'response': response.choices[0].message.content})
    except openai.error.OpenAIError as e:
        return Response({
            'error': f'OpenAI API error: {str(e)}'
        }, status=status.HTTP_503_SERVICE_UNAVAILABLE)
    except Exception as e:
        return Response({
            'error': f'Unexpected error: {str(e)}'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def GptAssistanceView(request):
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    validation_error = GPTConfig.validate_request_data(data)
    if validation_error:
        return validation_error
    
    if not data.get('problem'):
        return JsonResponse({'error': 'Missing problem description'}, status=400)

    try:
        user_content = (
            f"{GPTConfig.create_user_content(data)}\n"
            f"這是我目前遇到的問題：\n{data['problem']}"
        )

        response = openai.chat.completions.create(
            model=GPTConfig.MODEL,
            messages=[
                {'role': 'system', 'content': GPTConfig.ASSISTANCE_SYSTEM_CONTENT},
                {'role': 'user', 'content': user_content}
            ]
        )

        Gptassistance.objects.create(
            user=request.user,
            diary_id=data.get('diary_id'),
            interaction_time=data.get('date'),
            user_input=data['problem'],
            gpt_response=response.choices[0].message.content
        )

        return Response({
            'response': response.choices[0].message.content
        })

    except openai.error.OpenAIError as e:
        return Response({
            'error': f'OpenAI API error: {str(e)}'
        }, status=status.HTTP_503_SERVICE_UNAVAILABLE)
    except Exception as e:
        return Response({
            'error': f'Unexpected error: {str(e)}'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)