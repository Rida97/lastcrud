from django.shortcuts import render, redirect
from django import db
from django.http import HttpResponse
from .form import EmployeeCreate, SalaryCreate
from .models import Employee, Salary


def index(request):
    salaries = Salary.objects.all()
    return render(request, "base.html", {'salaries': salaries})


def create_emp(request):
    if request.method == 'POST':
        emp = EmployeeCreate(request.POST)
        if emp.is_valid():
            emp.save()
           # create_sal(request)
            return redirect('create-sal')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        emp = EmployeeCreate()
     #   sal = SalaryCreate()

    return render(request, 'create.html', {'employee': emp})


def create_sal(request):
    if request.method == 'POST':
        sal = SalaryCreate(request.POST)
        if sal.is_valid():
            sal.save()
        #    return redirect('index')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        sal = SalaryCreate()

    return render(request, 'create.html', {'sal': sal})

def update_emp(request, emp_id):
    try:
        employee_update = Employee.objects.get(id=emp_id)
    except Employee.DoesNotExist:
        return redirect('index')
    employee = EmployeeCreate(request.POST or None, instance=employee_update)
    if employee.is_valid():
        employee.save()
        employee_id = employee.id
        return redirect('update_sal', employee_id)

    #update_sal(request, employee)
       # return redirect('index')
    return render(request, 'create.html', {'employee':employee})

def update_sal(request, emp_id):
    try:
        sal_update = Salary.objects.get(pk=emp_id)
    except Salary.DoesNotExist:
        return redirect('index')
    new_sal = SalaryCreate(request.POST or None, instance=sal_update)
    if new_sal.is_valid():
        new_sal.save()
    return render(request, 'create.html', {'sal': new_sal})



def delete_emp(request, emp_id):
    try:
        emp_eliminate = Employee.objects.get(id=emp_id)
    except Employee.DoesNotExist:
        return redirect('index')
    emp_eliminate.delete()
    return redirect('index')




