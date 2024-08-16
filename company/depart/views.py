from .serializers import DepartmentSerializer, EmployeeSerializer
from rest_framework import status, viewsets
from rest_framework.response import Response
from .models import Departament, Employee
from pagination import CustomPagination
from permissions import IsAdminOrReadOnly, IsAdminOrReadOnlyOrIsAuthenticated


class DepartmentViewSet(viewsets.ModelViewSet):
    """
    ViewSet для работы с тегами.
    Запросы доступны только администраторам.
    """
    queryset = Departament.objects.all()
    permission_classes = (IsAdminOrReadOnly,)
    serializer_class = DepartmentSerializer
    pagination_class = None


class EmployeeViewSet(viewsets.ModelViewSet):
    """
    ViewSet для работы с тегами.
    Запросы доступны только администраторам.
    """
    queryset = Employee.objects.all()
    permission_classes = (IsAdminOrReadOnlyOrIsAuthenticated,)
    serializer_class = EmployeeSerializer
    pagination_class = CustomPagination
