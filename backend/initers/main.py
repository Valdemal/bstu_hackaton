from django.db import transaction

from .base import IniterComposite
from .components import user


class MainIniter(IniterComposite):
    initers = user.MainIniter,

    @classmethod
    def start(cls):
        with transaction.atomic():
            super().start()
