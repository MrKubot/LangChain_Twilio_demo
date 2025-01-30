from django.contrib import admin
from .models import Department, Employee

# Register your models here.

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'role', 'department', 'phone_number',)
    list_filter = ('role', 'department',)
    search_fields = ('first_name', 'last_name', 'role',)

    def full_name(self, obj):
        return f'{obj.first_name} {obj.last_name}'
    full_name.short_description = 'Pracownik'

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'employee_count',)
    search_fields = ('name',)

    def employee_count(self, obj):
        return obj.employees.count()
    employee_count.short_description = 'Liczba pracownikow'