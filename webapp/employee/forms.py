from django.forms import ModelForm, EmailInput, PasswordInput

from employee.models import Employee


class EmployeeForm(ModelForm):
    #UNA TABLA
    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {
            'email':EmailInput(attrs={'type':'email'}),
            'password':PasswordInput(attrs={'type':'password'})
        }
