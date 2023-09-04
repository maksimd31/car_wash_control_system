from django.db import models


class Client(models.Model):
    license_plate = models.CharField(max_length=20, unique=True, verbose_name='Государственный номер')
    full_name = models.CharField(max_length=100, verbose_name='ФИО')
    phone_number = models.CharField(max_length=15, verbose_name='Номер телефона')
    car_model = models.CharField(max_length=50, verbose_name='Марка и модель автомобиля')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время добавления')

    def __str__(self):
        return self.full_name


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Клиент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')
    work_type = models.CharField(max_length=100, verbose_name='Вид работы')
    cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Стоимость')
    employee = models.CharField(max_length=100, verbose_name='Сотрудник выполневший работу')
    comment = models.TextField(blank=True, verbose_name='Комментарий')

    def __str__(self):
        return f"Заказ #{self.pk} - {self.client.full_name}"


class Employee(models.Model):
    full_name = models.CharField(max_length=100, verbose_name='ФИО сотрудника')
    position = models.CharField(max_length=100, verbose_name='Должность сотрудника')
    employment_date = models.DateField(verbose_name='Дата устройства на работу')
    phone_number = models.CharField(max_length=15, verbose_name='Номер телефона сотрудника')
    registration_address = models.CharField(max_length=150, verbose_name='Адрес регистрации')
    residential_address = models.CharField(max_length=150, verbose_name='Адрес проживания')

    def __str__(self):
        return self.full_name
