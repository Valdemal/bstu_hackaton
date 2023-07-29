from drf_spectacular.utils import extend_schema
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from user_app.models import *
from user_app.serializers import GroupSerializer, GroupSubjectSerializer, StudentSerializer, TeacherSerializer


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    @extend_schema(responses=StudentSerializer(many=True), description="Возвращает список студентов группы")
    @action(methods=['GET'], detail=True)
    def students(self, request, pk):
        serialized = StudentSerializer(Student.objects.filter(group__pk=pk), many=True)
        return Response(serialized.data)


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class GroupSubjectViewSet(ModelViewSet):
    queryset = GroupSubject.objects.all()
    serializer_class = GroupSubjectSerializer
