from django.shortcuts import render, redirect
from django import db
from django.http import HttpResponse
from .form import EmployeeCreate
from .models import Employee


def index(request):  # retrieve or read from db
    employee = Employee.objects.all()
    return render(request, "base.html", {'employee': employee})


def create_emp(request):
    employee = EmployeeCreate()
    if request.method == 'POST':
        employee = EmployeeCreate(request.POST)
        if employee.is_valid():
            employee.save()
            return redirect('index')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'create.html', {'employee': employee})


def update_emp(request, emp_id):
    try:
        employee_update = Employee.objects.get(id=emp_id)
    except Employee.DoesNotExist:
        return redirect('index')
    employee = EmployeeCreate(request.POST or None, instance=employee_update)
    if employee.is_valid():
        employee.save()
        return redirect('index')
    return render(request, 'create.html', {'employee':employee})


def delete_emp(request, emp_id):
    try:
        emp_eliminate = Employee.objects.get(id=emp_id)
    except Employee.DoesNotExist:
        return redirect('index')
    emp_eliminate.delete()
    return redirect('index')

