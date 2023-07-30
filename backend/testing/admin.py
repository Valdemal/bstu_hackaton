from django.contrib import admin

from .models import Test, AssignedTest, Answer, Question

for model in [
    Test, AssignedTest, Answer, Question
]:
    admin.site.register(model)
