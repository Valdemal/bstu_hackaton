import random
import string

from django.contrib.auth import get_user_model

from initers.base import Initer

User = get_user_model()

USERNAME = "admin"
PASSWORD_LETTERS = string.ascii_letters + string.digits
PASSWORD = ''.join(
    random.choice(PASSWORD_LETTERS) for _ in range(random.randint(20, 30))
)


class MainIniter(Initer):
    @classmethod
    def start(cls):
        User.objects.create_superuser(username=USERNAME, password=PASSWORD)
