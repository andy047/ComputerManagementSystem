from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from device.forms import DeviceForm
from device.models import Device


def devices(request):
    devices = Device.objects.all()
    return render(request,'devices.html', {'devices':devices})


def new_device(request):

    if request.method=='POST':
        device_form = DeviceForm(request.POST)
        if device_form.is_valid():
            device_form.save()
            return redirect('devices')
    else:
        device_form = {'device_form':DeviceForm()}
        return render(request,'new_device.html',device_form)


def new_dev_report(request):

    if request.method=='POST':
        device_form = DeviceForm(request.POST)
        if device_form.is_valid():
            device_form.save()
            return redirect('new_report')
    else:
        device_form = {'device_form':DeviceForm()}
        return render(request,'new_device.html',device_form)

def edit_device(request,id):
    device = get_object_or_404(Device,pk=id)

    if request.method=='POST':
        device_form = DeviceForm(request.POST,instance=device)
        if device_form.is_valid():
            device_form.save()
            return redirect('devices')
    else:
        device_form = DeviceForm(instance=device)
        return render(request,'edit_device.html', {'device_form':device_form})

def delete_device(request,id):
    device = get_object_or_404(Device,pk=id)
    device.delete()
    return redirect('devices')
