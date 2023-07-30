from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from dicts.models import EducationProgram, Subject


class User(AbstractUser):
    is_student = models.BooleanField(default=False, verbose_name="Статус студента")
    is_teacher = models.BooleanField(default=False, verbose_name="Статус преподавателя")

    def __str__(self):
        if self.first_name and self.last_name:
            return f"{self.last_name} {self.first_name}"
        else:
            return str(self.username)


class Group(models.Model):
    name = models.CharField("Название", max_length=20, unique=True)
    education_program = models.ForeignKey(EducationProgram, on_delete=models.PROTECT, verbose_name="Программа обучения")

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Учебная группа'
        verbose_name_plural = 'Учебные группы'


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, verbose_name="Пользователь")
    group = models.ForeignKey(Group, on_delete=models.PROTECT, verbose_name="Учебная группа")
    markbook_id = models.CharField(max_length=30, verbose_name="Номер зачетной книжки")

    def __str__(self):
        return f"{self.group} {self.user}"

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, verbose_name="Пользователь")

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = "Преподаватель"
        verbose_name_plural = "Преподаватели"


# todo Проверить на совпадение компетенции преподавателя, дисциплины и программы группы
class GroupSubject(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name="Учебная группа")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name="Дисциплина")
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name="Преподаватель")

    def __str__(self):
        return f"{self.group} {self.subject}"

    class Meta:
        verbose_name = "Предмет, изучаемый группой"
        verbose_name_plural = "Предметы, изучаемые группами"


@receiver(post_save, sender=Student)
def tag_user_as_student(sender, instance: Student, created, **kwargs):
    if created:
        instance.user.is_student = True
        instance.user.save()


@receiver(post_save, sender=Teacher)
def tad_user_as_teacher(sender, instance: Teacher, created, **kwargs):
    if created:
        instance.user.is_teacher = True
        instance.user.save()


@receiver(post_delete, sender=Student)
def untag_user_as_student(sender, instance: Student, using, **kwargs):
    instance.user.is_student = False
    instance.user.save()


@receiver(post_delete, sender=Teacher)
def untag_user_as_teacher(sender, instance: Teacher, using, **kwargs):
    instance.user.is_teacher = False
    instance.user.save()
