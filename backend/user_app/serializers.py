from user_app.models import *
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'is_staff', 'is_student', 'is_teacher', 'first_name', 'last_name')
        read_only_fields = (
            'id', 'username', 'email', 'is_staff', 'is_student', 'is_teacher', 'first_name', 'last_name'
        )


class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Student
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Teacher
        fields = '__all__'


class GroupSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupSubject
        fields = '__all__'
