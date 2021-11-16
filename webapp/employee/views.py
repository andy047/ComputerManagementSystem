from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from employee.forms import EmployeeForm
from employee.models import Employee


def list_employees(request):
    objEmployees = Employee.objects.all()

    employees = {'employees':objEmployees}
    return render(request,'list_employees.html',employees)

def edit_employee(request,id):
    employee = get_object_or_404(Employee,pk=id)
    if request.method=='POST':
        employee_form = EmployeeForm(request.POST,instance=employee)
        if employee_form.is_valid():
            employee_form.save()
            return redirect('list_employees')
    else:
        employee_form = EmployeeForm(instance=employee)
        return render(request,'edit_employee.html',{'employee_form':employee_form})

def new_employee(request):

    if request.method=='POST':
        employee_form = EmployeeForm(request.POST)
        employee_form.save()
        return redirect('list_employees')
    else:
        employee_form = EmployeeForm()
        return render(request,'new_employee.html',{'employee_form':employee_form})


def delete_employee(request,id):
    employee = get_object_or_404(Employee,pk=id)
    employee.delete()
    return redirect('list_employees')