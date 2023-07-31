from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from testing.models import Test, Question, Answer, AssignedTest
from testing.serializers import TestSerializer, QuestionSerializer, AnswerSerializer, AssignedTestSerializer

from .filters import AnswerFilter, AssignedTestFilter


class TestViewSet(viewsets.ModelViewSet):
    serializer_class = TestSerializer

    def get_queryset(self):
        queryset = Test.objects.all()

        if self.request.user.is_authenticated:
            if self.request.user.is_staff:
                return queryset
            elif self.request.user.is_teacher:
                return queryset.filter(teacher__user=self.request.user)

        return queryset.none()


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswerViewSet(viewsets.ModelViewSet):
    serializer_class = AnswerSerializer
    filter_backends = DjangoFilterBackend,
    filterset_class = AnswerFilter

    def get_queryset(self):
        queryset = Answer.objects.all()

        if self.request.user.is_authenticated:
            if self.request.user.is_staff:
                return queryset
            elif self.request.user.is_teacher:
                return queryset.filter(assigned_test__test__teacher__user=self.request.user)
            elif self.request.user.is_student:
                return queryset.filter(assigned_test__student__user=self.request.user)

        return queryset.none()


class AssignedTestViewSet(viewsets.ModelViewSet):
    serializer_class = AssignedTestSerializer
    filter_backends = DjangoFilterBackend,
    filterset_class = AssignedTestFilter

    def get_queryset(self):
        queryset = AssignedTest.objects.all()

        if self.request.user.is_authenticated:
            if self.request.user.is_staff:
                return queryset
            elif self.request.user.is_teacher:
                return queryset.filter(test__teacher__user=self.request.user)
            elif self.request.user.is_student:
                return queryset.filter(student__user=self.request.user)

        return queryset.none()
