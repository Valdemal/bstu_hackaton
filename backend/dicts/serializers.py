from rest_framework import serializers
from dicts.models import *


class SpecialtySerializer(serializers.ModelSerializer):
    class Meta:
        model = Speciality
        fields = '__all__'


class UgsnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ugsn
        fields = '__all__'


class CompetenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competence
        fields = '__all__'


class IndicatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indicator
        fields = '__all__'


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class EducationProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationProgram
        fields = '__all__'
