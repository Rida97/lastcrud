from django.db import models
import uuid


class Employee(models.Model):
    department = models.ForeignKey('Department', on_delete=models.CASCADE) # MANY TO ONE R/SHIP
    name = models.CharField(max_length=20, null=False)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.name


class Salary(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, primary_key=True)
    salary = models.IntegerField(null=False)
    bankname = models.CharField(max_length=20, default="no bank info")

    def __str__(self):
        return str(self.salary)


class Department(models.Model):
    deptname = models.CharField(max_length=10, null=False, blank=False)

    def __str__(self):
        return self.deptname









