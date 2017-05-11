from datetime import datetime

from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from api.models import Employer, Employee


class ApiViewsTest(APITestCase):
    def setUp(self):
        self.employer = Employer.objects.create(
            name="Andela", location="US", email="contactus@andela.com")
        self.employee = Employee.objects.create(
            first_name="Lade", last_name="Oshodi", dob=datetime.strptime("04/29/1992", '%m/%d/%Y'), verified=True,
            employer=self.employer)

    def test_can_create_employer(self):
        url = reverse('employer-list')
        data = {'name': 'Andela', 'location': 'US', 'email': 'contactus@andela.com'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_can_create_employee(self):
        url = reverse('employee-list')
        data = {'first_name': 'Lade', 'last_name': 'Oshodi', 'dob': '1992-04-29',
                'verified': True, 'employer': self.employer.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
