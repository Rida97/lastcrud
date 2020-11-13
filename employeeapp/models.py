from django.db import models
import uuid


class Employee(models.Model):
   # emp_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
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

 # one dept can have many employees : Master table -> Employee , Foreign Table -> Dept -> it will have the fk employee


#class Department(models.Model):
 #   employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
  #  deptname = models.CharField(max_length=10, null=False, blank=False)






