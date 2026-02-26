from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Employee, Attendance
from .serializers import EmployeeSerializer, AttendanceSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'employeeId'

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        employee_id = self.request.query_params.get('employee_id', None)
        if employee_id is not None:
            queryset = queryset.filter(employee__employeeId=employee_id)
        return queryset
