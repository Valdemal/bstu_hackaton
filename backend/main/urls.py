from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/', include('djoser.urls.base')),
    path('api/auth/', include('djoser.urls.authtoken')),
]

schema_view = get_schema_view(
    openapi.Info(
        title="Project API",
        default_version='v1'),
    patterns=urlpatterns,
    public=True,
    permission_classes=[permissions.AllowAny, ]
)

urlpatterns.append(path('api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'))

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
