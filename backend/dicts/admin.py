from django.contrib import admin

from .models import *

for model in [
    Ugsn, Speciality, Competence, Indicator, Subject, EducationProgram
]:
    admin.site.register(model)
