from django.forms import ModelForm

from device.models import Device


class DeviceForm(ModelForm):
    class Meta:
        model = Device
        fields = '__all__'
"""
        widgets = {
            'email': EmailInput(attrs={'type': 'email'})
        }
"""