from django.urls import path
from .views import create_new_client

app_name = 'client'

urlpatterns = [
    path('create/', create_new_client, name='create_new_client'),
    # path('result/', result_page, name='result_page'),
]
