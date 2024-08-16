from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (DepartmentViewSet, EmployeeViewSet)

app_name = 'depart'


router = DefaultRouter()
router.register('departments', DepartmentViewSet, basename='departmens')
router.register('employee', EmployeeViewSet, basename='employee')

urlpatterns = [
    path('', include(router.urls)),
]
