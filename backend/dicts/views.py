from rest_framework.viewsets import ModelViewSet

from dicts.serializers import *


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
    serializer_class = IndicatorSerializer


class SubjectViewSet(ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class EducationProgramViewSet(ModelViewSet):
    queryset = EducationProgram.objects.all()
    serializer_class = EducationProgramSerializer
