from django.contrib import admin
from django.urls import path
from api.views import QuizList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/active-quizes', QuizList.as_view(), name='active-quizes')
]
