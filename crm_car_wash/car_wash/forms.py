from django import forms
from .models import Client, Order, Employee


# filename forms.py
class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


# filename forms.py
class ClientUpdateForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['full_name', 'phone_number', 'car_model']


# filename forms.py
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['client', 'work_type', 'cost', 'employee', 'comment']


# filename forms.py


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('first_name', 'last_name', 'position', 'department')


