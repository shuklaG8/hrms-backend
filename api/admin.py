from django.contrib import admin
from .models import Employee, Attendance

# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employeeId', 'fullName', 'email', 'department')
    search_fields = ('employeeId', 'fullName', 'email')
    list_filter = ('department',)

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('employee', 'date', 'status')
    list_filter = ('date', 'status')
    search_fields = ('employee__fullName', 'employee__employeeId')
    date_hierarchy = 'date'
