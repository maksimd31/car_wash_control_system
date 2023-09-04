from django import forms
from .models import Client, Order


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


class ClientUpdateForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['full_name', 'phone_number', 'car_model']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['client', 'work_type', 'cost', 'employee', 'comment']
