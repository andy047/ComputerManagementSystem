from django.db import models

# Create your models here.
from customer.models import Customer
from device.models import Device
from employee.models import Employee


class Report(models.Model):
    date_created = models.DateTimeField(auto_now=True)
    is_actived = models.BooleanField(default=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)  # Every report
    device = models.ForeignKey(Device, on_delete=models.SET_NULL,
                               null=True)  # es obligatorio que cada reporte tenga su equipo
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    deposit = models.CharField(max_length=200,null=True)
    serviceCost = models.CharField(max_length=200,null=True)
    total = models.CharField(max_length=200,null=True)
