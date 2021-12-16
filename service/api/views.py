from rest_framework import generics
from rest_framework.response import Response
from .serializers import QuizSerializer
from .models import Quiz


class QuizList(generics.ListAPIView):
    """View для получения списка активных опросов"""
    queryset = Quiz.objects.all()    
    serializer_class = QuizSerializer

    def list(self, request):
        """Метод для отсортировки только активных опросов для вывода"""
        queryset = self.get_queryset()
        queryset = list(filter(Quiz.is_active, queryset))
        serializer = QuizSerializer(queryset, many=True)

        return Response(serializer.data)
