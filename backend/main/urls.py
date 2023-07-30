from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView

from dicts.views import *
from user_app.views import *
from testing.views import *

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'specialities', SpecialityViewSet, 'specialities')
router.register(r'ugsns', UgsnViewSet, 'ugsns')
router.register(r'competences', CompetenceViewSet, 'competences')
router.register(r'indicators', IndicatorViewSet, 'indicators')
router.register(r'subjects', SubjectViewSet, 'subjects')
router.register(r'education-programs', EducationProgramViewSet, 'education-programs')

router.register(r'groups', GroupViewSet, 'groups')
router.register(r'students', StudentViewSet, 'students')
router.register(r'teachers', TeacherViewSet, 'teachers')
router.register(r'group-subjects', GroupSubjectViewSet, 'group-subjects')

router.register(r'tests', TestViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'answers', AnswerViewSet)
router.register(r'assigned-tests', AssignedTestViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/', include('djoser.urls.base')),
    path('api/auth/', include('djoser.urls.authtoken')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
