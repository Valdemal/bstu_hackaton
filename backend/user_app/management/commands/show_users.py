from django.core.management.base import BaseCommand
from django.conf import settings
from user_app.models import User
from initers.components.user_app import PASSWORD


class Command(BaseCommand):
    help = 'Выводит список пользователей системы'

    def handle(self, *args, **options):
        if not settings.DEBUG:
            print("Команда работает только в режиме отладки")
            return

        self.print_users("Студенты", User.objects.filter(is_student=True))
        self.print_users("Преподаватели", User.objects.filter(is_teacher=True))
        self.print_users("Администраторы", User.objects.filter(is_staff=True))

        print("Пароль у всех пользователей:", PASSWORD)

    @staticmethod
    def print_users(title: str, user_queryset):
        print(title + ':')
        for user in user_queryset:
            Command.print_user(user)

    @staticmethod
    def print_user(user: User):
        print(f"\t{user.username}")
