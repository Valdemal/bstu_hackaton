from django.contrib import admin

from .models import User, Student, Teacher, Group, GroupSubject

for model in [
    Student, Teacher, Group, GroupSubject, User
]:
    admin.site.register(model)
