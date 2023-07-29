from django.db import models


class EducationLevel(models.TextChoices):
    BACHELOR = 'Бакалавриат'
    SPECIALIST = 'Специалитет'
    MASTER = 'Магистратура'


class Ugsn(models.Model):
    name = models.CharField("Наименование", max_length=255)
    code = models.CharField("Код", max_length=20)

    def __str__(self):
        return str(self.code) + " " + str(self.name)

    class Meta:
        verbose_name = 'Укрупнённая группа специальности / направления'
        verbose_name_plural = 'Укрупнённые группы специальностей и направлений'


class Speciality(models.Model):
    name = models.CharField("Наименование", max_length=500)
    code = models.CharField("Код", max_length=20)
    level = models.CharField("Уровень образования", max_length=20, choices=EducationLevel.choices)
    ugsn = models.ForeignKey(Ugsn, on_delete=models.CASCADE, verbose_name='УГСН')

    def __str__(self):
        return f"{self.code} {self.name} ({self.level})"

    class Meta:
        verbose_name = 'Направление подготовки (специальность)'
        verbose_name_plural = 'Справочник направлений подготовки'


class Competence(models.Model):
    name = models.CharField("Наименование", max_length=255)
    category_name = models.CharField("Наименование категории", max_length=255)
    code = models.CharField('Код', max_length=50)
    level = models.CharField("Уровень образования", max_length=20, choices=EducationLevel.choices)

    def __str__(self):
        return f"{self.code} {self.name}"

    class Meta:
        verbose_name = "Компетенция"
        verbose_name_plural = "Компетенции"
        unique_together = ('name', 'code', 'level'),


class Indicator(models.Model):
    name = models.CharField("Наименование", max_length=700)
    code = models.CharField('Код', max_length=50)
    competence = models.ForeignKey(Competence, on_delete=models.CASCADE, verbose_name="Компетенция")

    def __str__(self):
        return f"{self.code} {self.name}"

    class Meta:
        verbose_name = "Индикатор"
        verbose_name_plural = "Индикаторы"
        unique_together = ('code', 'competence'),


class Subject(models.Model):
    name = models.CharField("Наименование", max_length=500, unique=True)
    competences = models.ManyToManyField(Competence, related_name="subjects", verbose_name="Компетенции")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Дисциплина"
        verbose_name_plural = "Дисциплины"


class EducationProgram(models.Model):
    name = models.CharField("Наименование", max_length=255)
    speciality = models.ForeignKey(Speciality, on_delete=models.PROTECT, verbose_name="Направление подготовки")
    subjects = models.ManyToManyField(Subject, verbose_name="Дисциплины")

    def __str__(self):
        return f"{self.name} ({self.speciality.level})"

    class Meta:
        verbose_name = 'Образовательная программа'
        verbose_name_plural = 'Образовательные программы'
        unique_together = ('name', 'speciality'),
