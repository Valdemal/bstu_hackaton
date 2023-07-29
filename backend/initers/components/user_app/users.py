import random

from initers.base import Initer, IniterComposite
from user_app.models import Student, User, Group, Teacher

USERNAME = "admin"
PASSWORD = 'ab123456'


class SuperuserIniter(Initer):
    @classmethod
    def start(cls):
        User.objects.create_superuser(username=USERNAME, password=PASSWORD)


class StaffUserIniter(Initer):
    @classmethod
    def start(cls):
        User.objects.create_user(
            username="staff_user", password=PASSWORD, first_name="Персонал", last_name="Персоналов", is_staff=True
        )


class StudentIniter(Initer):
    fixtures = (
        ("ivanov", "Иванов", "Иван", "ТЛ-121"),
        ("nickolaev", "Николаев", "Николай", "ТЛ-121"),
        ("kuzmin", "Кузьмин", "Кузьма", "ТЛ-121"),
        ("alexandrova", "Александрова", "Александра", "ТЛ-122"),
        ("andreeva", "Андреева", "Татьяна", "ТЛ-122"),
        ("tolstoi", "Толстой", "Лев", "ТЛ-122"),
        ("pushkin", "Пушкин", "Александр", "ЭБ-12"),
        ("ahmatova", "Ахматова", "Анна", "ЭБ-12"),
        ("tsvetaeva", "Цветаева", "Мария", "ЭБ-12"),
        ("chehov", "Чехов", "Антон", "ИТ-201"),
        ("dostoevsky", "Достоевский", "Федор", "ИТ-201"),
        ("gogol", "Гоголь", "Николай", "ИТ-201"),
        ("platonov", "Платонов", "Андрей", "ИТ-203"),
        ("sholohov", "Михаил", "Шолохов", "ИТ-203"),
        ("pasternak", "Пастернак", "Борис", "ИТ-203"),
    )

    @classmethod
    def start(cls):
        markbook_ids_samples = random.sample(range(1, 200000000), len(cls.fixtures))

        for i in range(len(cls.fixtures)):
            args = cls.fixtures[i]

            user = User.objects.create_user(
                username=args[0], password=PASSWORD, first_name=args[2], last_name=args[1]
            )

            Student.objects.create(
                user=user, group=Group.objects.get(name=args[3]), markbook_id=markbook_ids_samples[i]
            )


class TeacherIniter(Initer):
    fixtures = (
        ('karamzin', "Карамзин", "Николай"),
        ('derzhavin', "Державин", "Гавриил"),
        ('lomonosov', "Ломоносов", "Михаил"),
    )

    @classmethod
    def start(cls):
        for args in cls.fixtures:
            Teacher.objects.create(user=User.objects.create_user(
                username=args[0], last_name=args[1], first_name=args[2], password=PASSWORD
            ))


class UsersIniter(IniterComposite):
    initers = SuperuserIniter, StaffUserIniter, StudentIniter, TeacherIniter
