from django.shortcuts import render, redirect


# Create your views here.
from employee.models import Employee
from report.models import Report


def index(request):

    if request.session.keys():
        reports = {'reports': Report.objects.all()}
        return render(request, 'index.html', reports)
    else:
        return redirect('login')


def login(request):

    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        if Employee.objects.filter(username=username,password=password).exists():
            employee = Employee.objects.get(username=username)
            request.session['username']=employee.username
            return redirect('index')
        else:
            print('user do not exits')
            return render(request,'login.html')
    else:
        return render(request,'login.html')


def logout(request):
    del request.session['username']
    #del request.session['employee']
    return redirect('login')


