from rest_framework import serializers
from .models import Employee, Attendance

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class AttendanceSerializer(serializers.ModelSerializer):
    employee = serializers.SlugRelatedField(
        queryset=Employee.objects.all(),
        slug_field='employeeId'
    )
    employee_name = serializers.CharField(source='employee.fullName', read_only=True)
    employee_id = serializers.CharField(source='employee.employeeId', read_only=True)

    class Meta:
        model = Attendance
        fields = ['id', 'employee', 'employee_name', 'employee_id', 'date', 'status']
