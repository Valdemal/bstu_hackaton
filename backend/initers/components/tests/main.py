import random
from datetime import datetime, timedelta

from initers.base import IniterComposite, Initer
from testing.models import *
from dicts.models import *
from user_app.models import *


class TestIniter(Initer):
    @classmethod
    def start(cls):
        for teacher in Teacher.objects.all():
            available_group_subjects = GroupSubject.objects.filter(teacher=teacher)
            for i in range(random.randint(3, 5)):
                name = "Тест " + str(random.randint(1, 100))

                subject = random.choice(available_group_subjects).subject
                competence = subject.competences.first()
                available_indicators = list(Indicator.objects.filter(competence=competence))
                indicators = random.sample(
                    available_indicators, len(available_indicators)
                )

                test = Test.objects.create(name=name, teacher=teacher, subjects=subject)

                for indicator in indicators:
                    test.indicators.add(indicator)


class QuestionIniter(Initer):
    QUESTIONS_COUNT = 5

    @classmethod
    def start(cls):
        for test in Test.objects.all():
            for i in range(cls.QUESTIONS_COUNT):
                text = "Пример вопроса №" + str(i+1) + " к тесту "
                correct_answer = "Пример правильного ответа на " + text
                Question.objects.create(test=test, correct_answer=correct_answer, text=text)


class AssignedTestIniter(Initer):
    @classmethod
    def start(cls):
        for test in Test.objects.all():
            available_students = list(Student.objects.filter(group__groupsubject__teacher=test.teacher).distinct())
            end_time = datetime.now() + timedelta(days=1)

            for student in random.sample(available_students, random.randint(1, len(available_students))):
                AssignedTest.objects.create(test=test, student=student, end_time=end_time)


class AnswerIniter(Initer):
    @classmethod
    def start(cls):
        for assigned_test in AssignedTest.objects.all():
            questions = Question.objects.filter(test=assigned_test.test)
            for question in questions:
                is_correct_answer = bool(random.randint(0, 1))\

                if is_correct_answer:
                    answer_text = question.correct_answer
                else:
                    answer_text = f"Неправильный ответ на вопрос {question}"

                Answer.objects.create(question=question, answer=answer_text)


class MainIniter(IniterComposite):
    initers = TestIniter, QuestionIniter, AssignedTestIniter, AnswerIniter
