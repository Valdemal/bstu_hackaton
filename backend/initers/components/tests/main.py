import random

from initers.base import IniterComposite, Initer
from testing.models import *
from dicts.models import *
from user_app.models import *


class TestIniter(Initer):

    @classmethod
    def start(cls):
        for teacher in Teacher.objects.all():
            avaliable_group_subjects = GroupSubject.objects.filter(teacher=teacher)
            for i in range(random.randint(3, 5)):
                name = "Тест " + str(random.randint(1, 100))

                subject = random.choice(avaliable_group_subjects).subject
                competence = subject.competences.first()
                avaliable_indicators = list(Indicator.objects.filter(competence=competence))
                # todo пофиксить
                indicators = random.sample(
                    avaliable_indicators, len(avaliable_indicators)
                )

                test = Test.objects.create(name=name, teacher=teacher, subjects=subject)

                for indicator in indicators:
                    test.indicators.add(indicator)


class QuestionIniter(Initer):
    fixtures = (
        "Вопрос 1",
        "Вопрос 2",
        "Вопрос 3",
        "Вопрос 4",
        "Вопрос 5",
    )

    @classmethod
    def start(cls):
        pass
#         tests = Test.objects.all()
#         for args in cls.fixtures:
#             test = random.choice(tests)
#             correct_answer = random.choice(Answer.objects.all())
#             Question.objects.create(test=test, correct_answer=correct_answer, text=args)


class AnswerIniter(Initer):
    fixtures = (
        "Ответ 1",
        "Ответ 2",
        "Ответ 3",
        "Ответ 4",
        "Ответ 5",
    )

    @classmethod
    def start(cls):
        pass


class AssignedTestIniter(Initer):
    fixtures = (
    )

    @classmethod
    def start(cls):
        pass


class MainIniter(IniterComposite):
    initers = TestIniter, QuestionIniter, AnswerIniter, AssignedTestIniter
