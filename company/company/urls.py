from django.contrib import admin
from django.urls import path, include
# from rest_framework import routers
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi


# schema_view = get_swagger_view(title='API documentation')

urlpatterns = [
    path('admin/', admin.site.urls),
    # path(r'^swagger/$', schema_view),
    path('api/', include('users.urls', namespace='users')),
    path('api/', include('depart.urls', namespace='depart')),
]
