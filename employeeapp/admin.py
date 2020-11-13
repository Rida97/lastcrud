from django.contrib import admin
from .models import Employee, Salary, Department

admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Salary)

