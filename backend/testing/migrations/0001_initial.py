# Generated by Django 4.1.2 on 2023-07-30 00:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dicts', '0005_alter_competence_category_name_alter_competence_name_and_more'),
        ('user_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssignedTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('end_time', models.DateTimeField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_app.student')),
            ],
            options={
                'verbose_name': 'Назначенный тест',
                'verbose_name_plural': 'Назначенные тесты',
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название теста')),
                ('indicators', models.ManyToManyField(to='dicts.indicator', verbose_name='Индикаторы')),
                ('students', models.ManyToManyField(related_name='assigned_tests', through='testing.AssignedTest', to='user_app.student')),
                ('subjects', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dicts.subject')),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user_app.teacher')),
            ],
            options={
                'verbose_name': 'Тест',
                'verbose_name_plural': 'Тесты',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=500)),
                ('correct_answer', models.JSONField(default=dict)),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testing.test')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
        migrations.AddField(
            model_name='assignedtest',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testing.test'),
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.JSONField(default=dict)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testing.question')),
            ],
            options={
                'verbose_name': 'Ответ на вопрос',
                'verbose_name_plural': 'Ответы на вопросы',
            },
        ),
    ]