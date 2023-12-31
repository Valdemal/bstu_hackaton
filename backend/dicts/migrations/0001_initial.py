# Generated by Django 4.1.2 on 2023-07-28 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Competence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Наименование')),
                ('category_name', models.CharField(max_length=255, unique=True, verbose_name='Наименование категории')),
                ('code', models.CharField(max_length=50, verbose_name='Код')),
            ],
            options={
                'verbose_name': 'Компетенция',
                'verbose_name_plural': 'Компетенции',
            },
        ),
        migrations.CreateModel(
            name='Ugsn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, verbose_name='Код')),
            ],
            options={
                'verbose_name': 'Укрупнённая группа специальности / направления',
                'verbose_name_plural': 'Укрупнённые группы специальностей и направлений',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, unique=True, verbose_name='Наименование')),
                ('competences', models.ManyToManyField(related_name='subjects', to='dicts.competence', verbose_name='Компетенции')),
            ],
            options={
                'verbose_name': 'Дисциплина',
                'verbose_name_plural': 'Дисциплины',
            },
        ),
        migrations.CreateModel(
            name='Speciality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, verbose_name='Наименование')),
                ('code', models.CharField(max_length=20, unique=True, verbose_name='Код')),
                ('level', models.CharField(choices=[('Бакалавриат', 'Bachelor'), ('Специалитет', 'Specialist'), ('Магистратура', 'Master')], max_length=20, verbose_name='Уровень образования')),
                ('ugsn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dicts.ugsn', verbose_name='УГСН')),
            ],
            options={
                'verbose_name': 'Направление подготовки (специальность)',
                'verbose_name_plural': 'Справочник направлений подготовки',
            },
        ),
        migrations.CreateModel(
            name='EducationProgram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Наименование')),
                ('speciality', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dicts.speciality', verbose_name='Направление подготовки')),
                ('subjects', models.ManyToManyField(to='dicts.subject', verbose_name='Дисциплины')),
            ],
            options={
                'verbose_name': 'Образовательная программа',
                'verbose_name_plural': 'Образовательные программы',
            },
        ),
        migrations.CreateModel(
            name='Indicator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование')),
                ('code', models.CharField(max_length=50, verbose_name='Код')),
                ('competence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dicts.competence', verbose_name='Компетенция')),
            ],
            options={
                'verbose_name': 'Индикатор',
                'verbose_name_plural': 'Индикаторы',
                'unique_together': {('code', 'competence')},
            },
        ),
    ]
