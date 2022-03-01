from django.contrib import admin
from .models import Student, Department

class StudentAdmin(admin.ModelAdmin):
    list_display = ('stdId', 'name', 'gender', 'email')

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')

admin.site.register(Student, StudentAdmin)
admin.site.register(Department, DepartmentAdmin)
