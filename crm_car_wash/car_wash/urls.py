from django.urls import path
from . import views
from django.urls import path
from . import views

urlpatterns = [
    path('new_order/', views.new_order, name='new_order'),
    path('add_client/', views.add_client, name='add_client'),
    path('calculate_price/', views.calculate_price, name='calculate_price'),
]


