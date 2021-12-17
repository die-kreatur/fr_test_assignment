from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils import timezone
from django.db import IntegrityError
from .serializers import QuestionSerializer, QuizSerializer, AnswerSerializer
from .models import Quiz, Question, Answer


class QuizList(generics.ListAPIView):
    """View для получения списка активных опросов"""
    today = timezone.now().date()
    queryset = Quiz.objects.filter(end__gte=today)
    serializer_class = QuizSerializer


class PostAnswers(APIView):
    """View для ответа на вопросы"""
    def get(self, request, pk, format=None):
        """Получение вопроса по его идентификатору"""
        try:
            question = Question.objects.get(pk=pk)
            serializer = QuestionSerializer(question, many=False)
            return Response(serializer.data)
        except Question.DoesNotExist:
            return Response(
                {'Error': f'Question number {pk} does not exist'},
                status=status.HTTP_405_METHOD_NOT_ALLOWED
                )


    def post(self, request, pk, format=None):
        """Отправка ответа на вопрос серверу и сохранение его в БД"""
        try:    
            question = Question.objects.get(pk=pk)
            quiz = question.quiz_id
            
            request.data['question'] = question.pk
            request.data['quiz'] = quiz

            serializer = AnswerSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save(
                    uid=request.session['user_id']
                )
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except IntegrityError:
            """Обработка ошибки, в случае если пользователь попытается ответить на вопрос снова"""
            return Response(
                {'Error': 'You have already answered this question'},
                status=status.HTTP_405_NOT_FOUND
                )


class GetAnswers(generics.ListAPIView):
    """Получение своих детализированныйх ответов пользователем на вопросы"""
    serializer_class = AnswerSerializer

    def get_queryset(self):
        user = self.request.session['user_id']
        return Answer.objects.filter(uid=user)
