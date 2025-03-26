from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from . import views
from django.conf import settings

urlpatterns = [
    # path('admin/', admin.site.urls),
    path("", views.home, name='home'), 
    path('auth/', include('users.urls')),
    path('healthcare/', include('healthcare.urls')),    
    path('chat/', include('chat.urls')),

    # 📄 API Schema & Docs
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("docs/swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("docs/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]


if getattr(settings, "ADMIN_ENABLED", False):  # Check if admin is enabled
    urlpatterns.append(path("secure-admin-panel/", admin.site.urls))  