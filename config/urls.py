
from django.contrib import admin
from django.urls import path, include

from books.swagger_config import schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('books.urls')),

    # DRF Authentication urls
    path('api/api-auth/', include('rest_framework.urls')),
    path('api/dj-rest-auth/', include('dj_rest_auth.urls')),
    path('api/dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),

    #     Swagger
    path('api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-swagger-ui'),
    path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
