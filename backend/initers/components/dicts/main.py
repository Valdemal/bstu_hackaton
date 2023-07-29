from abc import ABC, abstractmethod
from typing import Sequence

import openpyxl
from django.conf import settings

from dicts.models import Subject, EducationProgram, Speciality, Ugsn, Competence, Indicator, EducationLevel
from initers.base import Initer, IniterComposite


class ExcelSampleIniter(Initer, ABC):
    SAMPLES_DIR = settings.BASE_DIR / 'initers' / 'components' / 'dicts' / 'data_samples'

    files: Sequence[str] = ()
    column_count: int = 0

    @classmethod
    @abstractmethod
    def _init_from_row(cls, row: tuple, *args, **kwargs):
        pass

    @classmethod
    def start(cls):
        for filename in cls.files:
            cls._init_from_file(filename)

    @classmethod
    def _init_from_file(cls, filename, *args, **kwargs):
        ws = cls._get_active_worksheet(filename)
        for row in ws.iter_rows(values_only=True, min_row=2, max_col=cls.column_count):
            cls._init_from_row(row, *args, **kwargs)

    @classmethod
    def _get_active_worksheet(cls, filename: str):
        path = cls.SAMPLES_DIR / filename
        wb = openpyxl.load_workbook(filename=str(path))
        return wb.active


class SubjectIniter(ExcelSampleIniter):
    files = 'Дисциплины.xlsx',
    column_count = 1

    @classmethod
    def _init_from_row(cls, row: tuple, *args, **kwargs):
        Subject.objects.get_or_create(name=row[0])


class EducationProgramsAndSpecialitiesIniter(ExcelSampleIniter):
    files = 'Справочник_бакалавриат.xlsx', 'Справочник_магистратура.xlsx', 'Справочник_специалитет.xlsx'
    column_count = 6

    @classmethod
    def _init_from_row(cls, row: tuple, *args, **kwargs):
        ugsn = Ugsn.objects.get_or_create(name=row[2], code=row[1])[0]
        speciality = Speciality.objects.get_or_create(name=row[4], code=row[3], level=row[0].title(), ugsn=ugsn)[0]

        EducationProgram.objects.create(name=row[5], speciality=speciality)


class CompetencesAndIndicatorsIniter(ExcelSampleIniter):
    files = 'УК_бакалавриат.xlsx', 'УК_магистратура.xlsx', 'УК_специалитет.xlsx'
    column_count = 5

    @classmethod
    def _init_from_row(cls, row: tuple, *args, **kwargs):
        competence = Competence.objects.filter(name=row[0], code=row[1], level=kwargs['level'])

        if competence.exists():
            competence = competence.first()
        else:
            competence = Competence.objects.create(
                name=row[0], code=row[1], category_name=row[2], level=kwargs['level'])

        Indicator.objects.create(name=row[4], code=row[3], competence=competence)

    @classmethod
    def start(cls):
        cls._init_from_file('УК_бакалавриат.xlsx', level=EducationLevel.BACHELOR)
        cls._init_from_file('УК_магистратура.xlsx', level=EducationLevel.MASTER)
        cls._init_from_file('УК_специалитет.xlsx', level=EducationLevel.SPECIALIST)


class MainIniter(IniterComposite):
    initers = SubjectIniter, EducationProgramsAndSpecialitiesIniter, CompetencesAndIndicatorsIniter
