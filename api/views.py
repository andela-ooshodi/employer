from rest_framework import mixins, viewsets

from .models import Employee, Employer

from .serializers import EmployeeSerializer, EmployerSerializer


class EmployerViewSet(viewsets.ModelViewSet):
    """
    Perform CRUD on employer
    """
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    """
    Perform CRUD on employee
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
