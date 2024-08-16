from rest_framework import serializers
from rest_framework.response import Response
from .models import Departament, Employee
from django.db.models import Sum


class DepartmentSerializer(serializers.ModelSerializer):
    '''
    Сериализатор для департаментов.
    '''

    number_of_employees = serializers.SerializerMethodField(read_only=True)
    total_salary = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Departament
        fields = (
            'id',
            'name',
            'number_of_employees',
            'total_salary'
        )

    def get_number_of_employees(self, obj):
        return obj.employee.all().count()
    
    def get_total_salary(self, obj):
        return obj.employee.all().aggregate(Sum('salary'))


class ShowEmployeeSerializer(serializers.ModelSerializer):
    '''
    Сериализатор для просмотра работников.
    '''

    full_name = serializers.SerializerMethodField(read_only=True)
    age = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Employee
        fields = (
            'full_name',
            'birth_date',
            'age',
            'depart',
            'position',
            'salary'
        )

    def get_full_name(self, obj):
        return obj.full_name

    def get_age(sefl, obj):
        return obj.get_age


class EmployeeSerializer(serializers.ModelSerializer):
    '''
    Сериализатор для обработки работников отдела.
    '''

    class Meta:
        model = Employee
        fields = (
            'name',
            'last_name',
            'birth_date',
            'depart',
            'position',
            'salary'
        )

    def to_representation(self, instance):
        request = self.context.get('request')
        context = {'request': request}
        return ShowEmployeeSerializer(instance, context=context).data
