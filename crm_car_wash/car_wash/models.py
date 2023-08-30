from django.db import models

# Create your models here.
from django.db import models


class Client(models.Model):
    """
    license_plate - гос номер
    name - фио
    phone_number - номер телефона
    car_model - марка модель автомобиля
    created_at - дата заполнения
    """
    license_plate = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    car_model = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} {self.license_plate} {self.phone_number} {self.car_model}'


class Order(models.Model):
    """
    client - клиент
    created_at - дата проведения услуги
    work_type - Выполненные работы
    cost - стоимость
    employee - работник выполнивший работу
    comment - комментарий
    """
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    work_type = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    employee = models.CharField(max_length=100)
    comment = models.TextField()

    def __str__(self):
        return f"Order for {self.client.name} {self.created_at} {self.work_type} {self.cost} {self.employee} " \
               f"{self.comment}"


class Employee(models.Model):
    """
    name - ф.и.о сотрудника
    position - должность
    hire_date - дата трудоустройства
    phone_number - телефонный номер
    registration_address - адрес регистрации
    residence_address - адрес проживания
    """
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    hire_date = models.DateField()
    phone_number = models.CharField(max_length=20)
    registration_address = models.TextField()
    residence_address = models.TextField()

    def __str__(self):
        return f'{self.name} {self.position} {self.hire_date} {self.phone_number} {self.residence_address}' \
               f'{self.registration_address}'
