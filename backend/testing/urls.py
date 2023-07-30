from django.urls import include, path
from rest_framework.routers import DefaultRouter

from testing.views import TestViewSet, QuestionViewSet, AnswerViewSet, AssignedTestViewSet

router = DefaultRouter()
router.register(r'tests', TestViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'answers', AnswerViewSet)
router.register(r'assigned-tests', AssignedTestViewSet)

urlpatterns = [
    path('testing/', include(router.urls)),
]