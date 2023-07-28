from abc import abstractmethod, ABC
from typing import List, Any, Callable, Dict, Sequence, Type

from django.db.models import Model


class Initer(ABC):
    """
    Абстрактный класс инитер
    """

    @classmethod
    @abstractmethod
    def start(cls):
        """Запускает инитер"""
        pass


class IniterComposite(Initer):
    """
    Компоновщик инитеров. По очереди запускает initers в порядке их следования
    """
    initers: Sequence[Initer] = ()

    @classmethod
    def start(cls):
        for initer in cls.initers:
            initer.start()


class ModelIniter(Initer):
    """
    Инитер модели.
    """

    # Модель, объекты которой должны быть созданы.
    model: Type[Model] = None

    # Последовательность наборов значений полей, которые должны быть переданы в конструктор модели
    cases: Sequence[Sequence[Any]] = ()

    # Последовательность названий полей, которые должны быть переданы в конструктор модели
    fields_names: Sequence[str] = ()

    @classmethod
    def start(cls):
        for case in cls.cases:
            cls.model.objects.create(**cls._case_to_kwargs(case))

    @classmethod
    def _case_to_kwargs(cls, case: Sequence[Any]) -> Dict[str, Any]:
        """
        Сопоставляет каждому названию поля значение из набора.

        @param case: Набор значений полей, которые должны быть переданы в конструктор модели
        @return **kwargs для метода Model.objects.create
        """

        return {cls.fields_names[i]: case[i] for i in range(len(cls.fields_names))}


def create_model_initer(
        model_: Type[Model],
        cases_: Sequence[Sequence[Any]],
        fields_names_: Sequence[str] = None,
        case_to_kwargs: Callable[[Sequence[Any]], Dict[str, Any]] = None) -> Type[ModelIniter]:
    """
    @param model_: Модель, объекты которой должны быть созданы.
    @param cases_: Последовательность наборов значений полей, которые должны быть переданы в конструктор модели.
    @param fields_names_: Последовательность названий полей, которые должны быть переданы в конструктор модели.
    @param case_to_kwargs: Функция, которая сопоставляет каждому названию поля значение из набора.

    @return: Новый подкласс ModelIniter
    """

    if fields_names_ is None and case_to_kwargs is None:
        raise Exception("Передайте в функцию field_names_ или case_to_kwargs!")

    class NewModelIniter(ModelIniter):
        model = model_
        cases = cases_
        fields_names = fields_names_

        @classmethod
        def _case_to_kwargs(cls, case: List[Any]) -> Dict[str, Any]:
            if case_to_kwargs is not None:
                return case_to_kwargs(case)
            else:
                return super()._case_to_kwargs(case)

    return NewModelIniter
