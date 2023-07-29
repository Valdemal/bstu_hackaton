from django.contrib.auth import get_user_model

from dicts.models import EducationProgram
from initers.base import IniterComposite, Initer
from initers.components.user_app.users import UsersIniter
from user_app.models import Group

User = get_user_model()


class GroupIniter(Initer):
    fixtures = (
        ("ТЛ-121", "Таможенная логистика"),
        ("ТЛ-122", "Таможенная логистика"),
        ("ЭБ-12", "Экономико-правовое обеспечение экономической безопасности"),
        ("ИТ-201", "Информационные системы и технологии"),
        ("ИТ-202", "Информационные системы и технологии"),
        ("ИТ-203", "Информационные системы и технологии")
    )

    @classmethod
    def start(cls):
        for args in cls.fixtures:
            education_program = EducationProgram.objects.filter(name=args[1]).first()
            Group.objects.create(name=args[0], education_program=education_program)


# class GroupSubjectIniter(Initer):
#     fixtures = (
#         ("ТЛ-121")
#     )
#
#     @classmethod
#     def start(cls):
#         pass

class MainIniter(IniterComposite):
    initers = GroupIniter, UsersIniter
