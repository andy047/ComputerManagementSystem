from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from customer.forms import CustomerForm
from customer.models import Customer


def customers(request):
    dbcustomers = Customer.objects.all()
    customerNo = Customer.objects.count()
    customers = {'customers':dbcustomers,
                 'customerNo':customerNo
                 }
    print('custemers: ',customers)
    return render(request,'customers.html',customers)


def new_customer(request):
    if request.method=='POST':
        customerForm = CustomerForm(request.POST)
        if customerForm.is_valid():
            customerForm.save()
            return redirect('customers')
    else:
        customerForm = CustomerForm()
        return render(request,'new_customer.html',{'customerForm':customerForm})


def new_cust_report(request):
    if request.method=='POST':
        customerForm = CustomerForm(request.POST)
        if customerForm.is_valid():
            customerForm.save()
            return redirect('new_report')
    else:
        customerForm = CustomerForm()
        return render(request,'new_customer.html',{'customerForm':customerForm})


def edit_customer(request,id):
    customer = get_object_or_404(Customer, pk=id)
    if request.method=='POST':
        customerform = CustomerForm(request.POST,instance=customer)
        if customerform.is_valid():
            customerform.save()
            return redirect('customers')
    else:
        customerForm = CustomerForm(instance=customer)
        return render(request,'edit_customer.html',{'customerForm': customerForm})

def delete_customer(request,id):
    customer = get_object_or_404(Customer,pk=id)
    customer.delete()
    return redirect('customers')
