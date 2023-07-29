import random
from django.contrib.auth import get_user_model

from dicts.models import EducationProgram, Subject
from initers.base import IniterComposite, Initer
from initers.components.user_app.users import UsersIniter
from user_app.models import Group, Teacher, GroupSubject

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


class GroupSubjectIniter(Initer):
    @classmethod
    def start(cls):
        teachers = Teacher.objects.all()
        subjects = Subject.objects.all()

        for group_args in GroupIniter.fixtures:
            group = Group.objects.get(name=group_args[0])
            group_subjects = random.choices(subjects, k=random.randint(3, 5))

            for group_subject in group_subjects:
                group_teacher = random.choice(teachers)
                GroupSubject.objects.create(
                    group=group, subject=group_subject, teacher=group_teacher
                )


class MainIniter(IniterComposite):
    initers = GroupIniter, UsersIniter, GroupSubjectIniter
