from datetime import datetime
from django.test import TestCase

from api.models import Employer, Employee


class ApiModelsTest(TestCase):
    def setUp(self):
        self.employer = Employer.objects.create(
            name="Andela", location="US", email="contactus@andela.com")
        self.employee = Employee.objects.create(
            first_name="Lade", last_name="Oshodi", dob=datetime.strptime("04/29/1992", '%m/%d/%Y'), verified=True,
            employer=self.employer)

    def test_can_retrieve_employer(self):
        pass

    def test_can_retrieve_employee(self):
        pass
