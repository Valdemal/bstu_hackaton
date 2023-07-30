from drf_spectacular.utils import extend_schema
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from testing.models import AssignedTest
from testing.serializers import AssignedTestSerializer
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


class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    @extend_schema(responses=StudentSerializer(many=True), description="Возвращает список всех студентов преподавателя")
    @action(methods=['GET'], detail=True)
    def students(self, request, pk):
        serialized = StudentSerializer(Student.objects.filter(group__groupsubject__teacher__user__pk=pk).distinct(),
                                       many=True)
        return Response(serialized.data)

    @extend_schema(responses=GroupSerializer(many=True), description="Возвращает список всех групп преподавателя")
    @action(methods=['GET'], detail=True)
    def groups(self, request, pk):
        serialized = GroupSerializer(Group.objects.filter(groupsubject__teacher__user__pk=pk).distinct(), many=True)
        return Response(serialized.data)


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    @extend_schema(
        responses=AssignedTestSerializer(many=True), description="Возвращает список всех тестов, назначенных студенту"
    )
    @action(methods=['GET'], detail=True)
    def assigned_tests(self, request, pk):
        queryset = AssignedTest.objects.filter(student__user__pk=pk).order_by('start_time')
        serialized = AssignedTestSerializer(queryset, many=True)
        return Response(serialized.data)


class GroupSubjectViewSet(ModelViewSet):
    queryset = GroupSubject.objects.all()
    serializer_class = GroupSubjectSerializer
