from django.urls import path

from . import views

# from .views import create_new_client

app_name = 'client'

urlpatterns = [
    # path('create/', create_new_client, name='create_new_client'),
    path('/add_client/', views.add_client, name='add_client'),
    path('/delete/', views.delete_client, name='delete_client'),
    path('client/<str:license_plate>/update/', views.update_client, name='update_client'),
    path('order/create/', views.create_order, name='create_order'),
    path('order/<int:order_id>/delete/', views.delete_order, name='delete_order'),
    path('order/<int:order_id>/update/', views.update_order, name='update_order'),
    path('order/list/', views.order_list, name='order_list'),
    # path('result/', result_page, name='result_page'),
]
