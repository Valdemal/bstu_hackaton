from django.db import models


class EducationLevel(models.TextChoices):
    BACHELOR = 'Бакалавриат'
    SPECIALIST = 'Специалитет'
    MASTER = 'Магистратура'


class Ugsn(models.Model):
    code = models.CharField("Код", max_length=20)
    models.CharField("Наименование", max_length=255)

    class Meta:
        verbose_name = 'Укрупнённая группа специальности / направления'
        verbose_name_plural = 'Укрупнённые группы специальностей и направлений'


class Speciality(models.Model):
    name = models.CharField("Наименование", max_length=500)
    code = models.CharField("Код", max_length=20, unique=True)
    level = models.CharField("Уровень образования", max_length=20, choices=EducationLevel.choices)
    ugsn = models.ForeignKey(Ugsn, on_delete=models.CASCADE, verbose_name='УГСН')

    class Meta:
        verbose_name = 'Направление подготовки (специальность)'
        verbose_name_plural = 'Справочник направлений подготовки'


class Competence(models.Model):
    name = models.CharField("Наименование", max_length=255, unique=True)
    category_name = models.CharField("Наименование категории", max_length=255, unique=True)
    code = models.CharField('Код', max_length=50)

    class Meta:
        verbose_name = "Компетенция"
        verbose_name_plural = "Компетенции"


class Indicator(models.Model):
    name = models.CharField("Наименование", max_length=255)
    code = models.CharField('Код', max_length=50)
    competence = models.ForeignKey(Competence, on_delete=models.CASCADE, verbose_name="Компетенция")

    class Meta:
        verbose_name = "Индикатор"
        verbose_name_plural = "Индикаторы"
        unique_together = ('code', 'competence'),


class Subject(models.Model):
    name = models.CharField("Наименование", max_length=500, unique=True)
    competences = models.ManyToManyField(Competence, related_name="subjects", verbose_name="Компетенции")

    class Meta:
        verbose_name = "Дисциплина"
        verbose_name_plural = "Дисциплины"


class EducationProgram(models.Model):
    name = models.CharField("Наименование", max_length=255, unique=True)
    speciality = models.ForeignKey(Speciality, on_delete=models.PROTECT, verbose_name="Направление подготовки")
    subjects = models.ManyToManyField(Subject, verbose_name="Дисциплины")

    class Meta:
        verbose_name = 'Образовательная программа'
        verbose_name_plural = 'Образовательные программы'
