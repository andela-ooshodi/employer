from rest_framework import serializers

from api.models import Employee, Employer


class EmployerSerializer(serializers.ModelSerializer):
    employees = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='employee-detail'
    )

    class Meta:
        model = Employer
        fields = ('name', 'location', 'email', 'employees')


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('first_name', 'last_name', 'dob', 'verified', 'employer')
