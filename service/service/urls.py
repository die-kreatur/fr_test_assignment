from django.contrib import admin
from django.urls import path
from api.views import QuizList, PostAnswers, GetAnswers


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/active-quizes', QuizList.as_view(), name='active-quizes'),
    path('api/questions/<int:pk>', PostAnswers.as_view(), name='post-answer'),
    path('api/answers/', GetAnswers.as_view(), name='get-answers')
]
