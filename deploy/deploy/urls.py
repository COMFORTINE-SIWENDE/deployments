from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Bookstore API",
        default_version='v1',
        description="API for managing bookstore inventory",
        contact=openapi.Contact(email="admin@bookstore.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    # Redirect root URL to Swagger documentation
    path('', RedirectView.as_view(url='/swagger/', permanent=False)),
    
    # Admin and API endpoints
    path('admin/', admin.site.urls),
    path('api/', include('deployment.urls')),
    
    # Documentation endpoints
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]