from __future__ import unicode_literals

from django.db import models


class Base(models.Model):
    email = models.EmailField(max_length=50)

    class Meta:
        abstract = True

    def __str__(self):
        """
        String representation of model
        :return:
        """
        return self.name


class Employer(Base):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)


class Employee(Base):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField()
    verified = models.BooleanField()
    employer = models.ForeignKey(Employer, related_name='employees')
