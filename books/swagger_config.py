from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title='Book List API',
        default_version='books',
        description='Library demo project',
        contact=openapi.Contact('oripovmirshod9@gmail.com'),
        terms_of_service='demo.com',
        license=openapi.License(name='demo license'),
    ),
    public=True,
    permission_classes=[permissions.IsAuthenticated, ],

)
