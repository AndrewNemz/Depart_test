from django.contrib import admin

from .models import Employee, Departament, DirectorDepart

class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'last_name',
        'position',
        'salary',
        'birth_date',
        'depart'
    )


class DepartmentAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


class DirectorDepartAdmin(admin.ModelAdmin):
    list_display = (
        'director',
        'depart'
    )


admin.site.register(DirectorDepart, DirectorDepartAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Departament, DepartmentAdmin)
