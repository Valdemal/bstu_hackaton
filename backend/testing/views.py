from django.shortcuts import render

from rest_framework import viewsets

from testing.models import Test, Question, Answer, AssignedTest
from testing.serializators import TestSerializer, QuestionSerializer, AnswerSerializer, AssignedTestSerializer


class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class AssignedTestViewSet(viewsets.ModelViewSet):
    queryset = AssignedTest.objects.all()
    serializer_class = AssignedTestSerializer
