from django.db import transaction

from .base import IniterComposite
from .components import user, dicts


class MainIniter(IniterComposite):
    initers = user.MainIniter, dicts.MainIniter

    @classmethod
    def start(cls):
        with transaction.atomic():
            super().start()
