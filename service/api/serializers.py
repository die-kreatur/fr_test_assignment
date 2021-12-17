from django.db.models import fields
from rest_framework import serializers
from .models import Quiz, Answer, Question


class QuizSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели опроса"""
    class Meta:
        model = Quiz
        fields = ['name', 'start', 'end']


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['quiz', 'question', 'type']


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['quiz', 'question', 'answer']
