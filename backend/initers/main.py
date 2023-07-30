from django.db import transaction

from .base import IniterComposite
from .components import user_app, dicts,tests


class MainIniter(IniterComposite):
    initers = dicts.MainIniter, user_app.MainIniter,tests.MainIniter

    @classmethod
    def start(cls):
        with transaction.atomic():
            super().start()
