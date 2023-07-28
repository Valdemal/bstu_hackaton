from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from dicts.models import *
from dicts.serializers import *
# Create your views here.

class SpecialityViewSet(ModelViewSet):
	queryset = Speciality.objects.all()
	serializer_class = SpecialtySerializer

class UgsnViewSet(ModelViewSet):
		queryset = Ugsn.objects.all()
		serializer_class = UgsnSerializer

class CompetenceViewSet(ModelViewSet):
	queryset = Competence.objects.all()
	serializer_class = CompetenceSerializer

class IndicatorViewSet(ModelViewSet):
	queryset = Indicator.objects.all()
	serializer_class = CompetenceSerializer

class SubjectViewSet(ModelViewSet):
	queryset = Subject.objects.all()
	serializer_class = CompetenceSerializer

class EducationProgramViewSet(ModelViewSet):
	queryset = EducationProgram.objects.all()
	serializer_class = EducationProgramSerializer