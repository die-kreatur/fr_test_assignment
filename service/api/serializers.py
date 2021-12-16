from rest_framework import serializers
from .models import Quiz


class QuizSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели опроса"""
    class Meta:
        model = Quiz
        fields = ['name', 'start', 'end']
