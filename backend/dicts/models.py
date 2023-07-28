from django.db import models


class EduLevelChoices(models.IntegerChoices):
    BACHELOR = 1, 'Бакалавриат'
    SPECIALIST = 2, 'Специалитет'
    MASTER = 3, 'Магистратура'


class DictUgsn(models.Model):
    """
    Справочник укрупённых груп
    """

    code = models.CharField("Код", max_length=20)
    models.CharField("Наименование", max_length=255)

    class Meta:
        verbose_name = 'Укрупнённая группа специальности / направления'
        verbose_name_plural = 'Укрупнённые группы специальностей и направлений'


class DictSpec(models.Model):
    """
    Справочник специальностей
    """

    name = models.CharField("Наименование", max_length=500)
    code = models.CharField("Код", max_length=20)
    old_code = models.CharField("Старый код", max_length=20, blank=True)
    level = models.PositiveIntegerField('ID', choices=EduLevelChoices.choices)
    ugsn = models.ForeignKey(DictUgsn, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Направление подготовки (специальность)'
        verbose_name_plural = 'Справочник направлений подготовки'


class DictCompetence(models.Model):
    """
    Справочник компетенций
    """
    name = models.CharField("Наименование", max_length=255)
    category_name = models.CharField("Наименование категории", max_length=255)
    code = models.CharField('Код', max_length=50)


class DictIndicator(models.Model):
    """
    Справочник индикаторов
    """
    name = models.CharField("Наименование", max_length=255)
    code = models.CharField('Код', max_length=50)
    competence = models.ForeignKey(DictCompetence, on_delete=models.CASCADE)


class DictSubject(models.Model):
    """
    Справочник дисциплин
    """
    name = models.CharField("Наименование", max_length=500)
    competences = models.ManyToManyField(DictCompetence, related_name="subjects")


class DictEduProgram(models.Model):
    """
    Справочник образовательных програм
    """

    name = models.CharField("Наименование", max_length=255)
    spec = models.ForeignKey(DictSpec, on_delete=models.SET_NULL)
    subjects = models.ManyToManyField(DictSubject)
