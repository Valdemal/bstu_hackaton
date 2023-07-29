from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from user_app.models import *
from user_app.serializers import GroupSerializer, GroupSubjectSerializer, StudentSerializer, TeacherSerializer
# Create your views here.

class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class GroupSubjectViewSet(ModelViewSet):
    queryset = GroupSubject.objects.all()
    serializer_class = GroupSubjectSerializer
