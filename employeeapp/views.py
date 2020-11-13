from django.http import HttpResponse
from django.shortcuts import render, redirect

from .form import EmployeeCreate, SalaryCreate
from .models import Employee, Salary


def index(request):
    salaries = Salary.objects.all()
    return render(request, "base.html", {'salaries': salaries})


def create(request):
    sal = SalaryCreate(request.POST)
    if request.method == 'POST':

        emp = EmployeeCreate(request.POST)

        if emp.is_valid():
            emp.save()

            sal = SalaryCreate(request.POST)
            if sal.is_valid():
                salary_object = sal.save(commit=False)
                salary_object.employee_id = emp.instance.pk
                salary_object.save()
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        emp = EmployeeCreate()

    return render(request, 'create.html', {'employee': emp, 'sal': sal})


def update(request, emp_id):
    try:
        get_sal = Salary.objects.get(pk=emp_id)
        get_employee = Employee.objects.get(id=emp_id)
    except (Employee.DoesNotExist, Salary.DoesNotExist):
        return redirect('index')
    employee = EmployeeCreate(request.POST or None, instance=get_employee)
    new_sal = SalaryCreate(request.POST or None, instance=get_sal)
    if employee.is_valid() or new_sal.is_valid():
        employee.save()
        new_sal.save()
        print(employee.instance.id)
        print(get_employee)
    return render(request, 'create.html', {'employee': employee, 'sal': new_sal})


def delete(request, emp_id):
    try:
        emp_eliminate = Employee.objects.get(id=emp_id)
    except Employee.DoesNotExist:
        return redirect('index')
    emp_eliminate.delete()
    return redirect('index')
