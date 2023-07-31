from django_filters import rest_framework as drf_filters

from .models import AssignedTest, Answer


class AssignedTestFilter(drf_filters.FilterSet):
    group = drf_filters.CharFilter(field_name='student__group')

    class Meta:
        model = AssignedTest
        fields = 'student', 'test', 'group'


class AnswerFilter(drf_filters.FilterSet):
    student = drf_filters.CharFilter(field_name='assigned_test__student')
    group = drf_filters.CharFilter(field_name='assigned_test__student__group')
    test = drf_filters.CharFilter(field_name='assigned_test__test')
    assigned_test = drf_filters.CharFilter(field_name='assigned_test')

    class Meta:
        model = Answer
        fields = 'student', 'group', 'test', 'assigned_test'
