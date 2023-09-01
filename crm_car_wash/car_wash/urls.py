from django.urls import path
from . import views
from django.urls import path
from . import views

urlpatterns = [
    # path('new_order/', views.new_order, name='new_order'),
    path('add_client/', views.add_client, name='add_client'),
    path('calculate_price/', views.calculate_price, name='calculate_price'),
    path('new-client/', views.new_client, name='new_client'),
    path('add-client/<str:license_plate>/', views.add_client, name='add_client'),
    path('calculate-price/<int:client_id>/', views.calculate_price, name='calculate_price'),
    path('save-order/<int:order_id>/', views.save_order, name='save_order'),
]


