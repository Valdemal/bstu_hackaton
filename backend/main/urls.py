from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/', include('djoser.urls.base')),
    path('api/', include('testing.urls')),
    path('api/auth/', include('djoser.urls.authtoken')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
