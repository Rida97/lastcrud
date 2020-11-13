from django import forms

from .models import Employee, Salary


class EmployeeCreate(forms.ModelForm):
    salary_amount = forms.IntegerField()
    bank_name = forms.CharField()

    class Meta:
        model = Employee
        fields = '__all__'


class SalaryCreate(forms.ModelForm):
    class Meta:
        model = Salary
        fields = ['salary', 'bankname']

        employee = forms.ModelMultipleChoiceField(queryset=Employee.objects.all(), widget=forms.CheckboxSelectMultiple)
