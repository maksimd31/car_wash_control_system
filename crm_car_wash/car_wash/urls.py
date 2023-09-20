from django.urls import path

from car_wash import views

# from .views import delete_employee, edit_employee

# from .views import create_new_client

app_name = 'client'

urlpatterns = [
    # path('create/', create_new_client, name='create_new_client'),
    path('', views.add_client, name='add_client'),
    path('add_client', views.add_client, name='add_client'),
    # path('/add_client/', views.add_client, name='add_client'),
    path('/delete/', views.delete_client, name='delete_client'),
    path('client/<str:license_plate>/update/', views.update_client, name='update_client'),
    path('order/create/', views.create_order, name='create_order'),
    path('order/<int:order_id>/delete/', views.delete_order, name='delete_order'),
    path('order/<int:order_id>/update/', views.update_order, name='update_order'),
    path('order/list/', views.order_list, name='order_list'),
    path('delete_employee/<int:employee_id>/', views.delete_employee, name='delete_employee'),
    path('employee/<int:employee_id>/edit/', views.edit_employee, name='edit_employee'),

    # path('result/', result_page, name='result_page'),
]
