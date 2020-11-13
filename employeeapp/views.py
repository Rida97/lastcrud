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
            return redirect('create-sal')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        emp = EmployeeCreate()
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

        get_employee = Employee.objects.get(id=emp_id)  # this returns the emp that needs to be updated -> emp_id is passed from base.html
    except Employee.DoesNotExist:
        return redirect('index')
    employee = EmployeeCreate(request.POST or None, instance=get_employee)  # emp that needs updation is passed here along with the data to be updated in req.POST
    if employee.is_valid():  # is_valid is form's built in func
        employee.save()
        print (employee.instance.id) # employee -> form of emp
        print (get_employee)
      #  return redirect('update_sal', get_employee.pk)
        return redirect('update-sal', emp_id=employee.instance.id)
    return render(request, 'create.html', {'employee': employee})


def update_sal(request, emp_id):
    try:
        get_sal = Salary.objects.get(pk=emp_id) # this allows me to display all employees and i can choose from those employees
    except Salary.DoesNotExist:
        return redirect('index')
    new_sal = SalaryCreate(request.POST or None, instance=get_sal)
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


