from django.db import models
from django.utils import timezone


class Quiz(models.Model):
    """Модель для опроса, содержащего вопросы для пользователей"""
    name = models.CharField(max_length=250)
    start = models.DateField(default=timezone.now, editable=False)
    end = models.DateField()

    class Meta:
        verbose_name = 'Quiz'
        verbose_name_plural = 'Quizes'

    def __str__(self):
        return f"Quiz {self.name}"


class Question(models.Model):
    """Модель для отдельного вопроса в опросе"""
    question_types = [
        ('text answer', 'text answer'),
        ('one answer', 'one answer'),
        ('multiple answers', 'multiple answers')
    ]

    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question = models.CharField(max_length=250)
    type = models.CharField(max_length=20, choices=question_types)

    def __str__(self):
        return f"Question from {self.quiz}"


class Answer(models.Model):
    """Модель для пользовательских ответов на вопросы"""
    uid = models.IntegerField() # уникальный идентификатор пользователя
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=250)
    time_answered = models.DateField(default=timezone.now, editable=False)
    
    class Meta:
        """Пользователь может отвечать только один раз на каждый вопрос"""
        unique_together = ['uid', 'question']

    def __str__(self):
        return f"Answer on {self.question} from {self.quiz}"
        