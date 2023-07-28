from django.core.management.base import BaseCommand


from initers.components import user
from initers.main import MainIniter


class Command(BaseCommand):
    help = 'Выполняет инициализацию БД сущностями необходимыми для работы приложения.'

    def handle(self, *args, **options):
        if options['password'] is not None:
            user.PASSWORD = options['password']

        print('Начало инициализации БД.')
        MainIniter.start()
        print('Инициализация выполнена!')
        print("Данные для входа в систему:")
        print("Логин: " + user.USERNAME)
        print("Пароль: " + user.PASSWORD)

    def add_arguments(self, parser):
        parser.add_argument(
            '-p',
            '--password',
            type=str,
            required=False,
            help='Задает пароль для пользователя admin.'
        )
