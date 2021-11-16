from django.forms import ModelForm

from customer.models import Customer


class CustomerForm(ModelForm):

    class Meta:
        model = Customer
        fields = '__all__'
        """
        widgets = {
            'telephoneNumber':TextInput(attrs={'type':'number'}),
            'phoneNumber':TextInput(attrs={'type':'number'})
        }
"""

