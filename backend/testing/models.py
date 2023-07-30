from django.db import models

from dicts.models import Subject, Indicator
from user_app.models import Teacher, Student


class Test(models.Model):
    name = models.CharField('Название теста', max_length=255)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name="Преподаватель")
    subjects = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name="Предмет")
    indicators = models.ManyToManyField(Indicator, verbose_name='Индикаторы')
    students = models.ManyToManyField(
        Student,
        through='AssignedTest',
        related_name='assigned_tests',
    )

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'


class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    correct_answer = models.JSONField(default=dict)

    def __str__(self):
        return f"{self.text}({self.test})"

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"


class AssignedTest(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField()

    def __str__(self):
        return f"{self.student} -- {self.test}"

    class Meta:
        verbose_name = "Назначенный тест"
        verbose_name_plural = "Назначенные тесты"


class Answer(models.Model):
    assigned_test = models.ForeignKey(AssignedTest, on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.JSONField(default=dict)

    @property
    def is_correct(self) -> bool:
        return self.answer == self.question.correct_answer

    class Meta:
        verbose_name = "Ответ на вопрос"
        verbose_name_plural = "Ответы на вопросы"

