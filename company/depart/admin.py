from django.contrib import admin

from .models import Director, Employee, Departament


class DirectorAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'last_name',
        'position',
        'salary',
        'birth_date'
    )


class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'last_name',
        'position',
        'salary',
        'birth_date'
    )


class DepartmentAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'boss'
    )


admin.site.register(Director, DirectorAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Departament, DepartmentAdmin)
