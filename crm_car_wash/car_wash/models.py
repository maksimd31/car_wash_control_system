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
    work_types = models.ManyToManyField('WorkType')
    employees = models.ManyToManyField('Employee')
    cost = models.DecimalField(max_digits=8, decimal_places=2)
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


class WorkType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Salary(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    salary_amount = models.DecimalField(max_digits=10, decimal_places=2)


'''
Примечания:
- В модели Order я использовал work_types и employees как поля типа ManyToManyField, чтобы иметь возможность 
добавлять несколько видов работ и сотрудников к одному заказу. Эти поля связаны с моделями WorkType и 
Employee соответственно.
- Модель WorkType представляет собой отдельную таблицу, которая содержит виды работ. 
- нужно добавить дополнительные поля (например, описание, ставка за работу и т. д.).
- после внесения изменений в модели, вам необходимо выполнить миграцию 
(python manage.py makemigrations и python manage.py migrate), чтобы изменения отразились в базе данных.
'''

'''
Примечания:
- В модели Client я использовал license_plate в качестве первичного ключа (primary key), так как 
он является государственным номером. 
- В модели Order я использовал внешний ключ (foreign key) client, связывающий заказ с клиентом. 
Нужно будет учесть, что делать, если клиент удаляется из базы данных, чтобы не возникало 
неконсистентных данных. В данном примере, я установил параметр on_delete=models.CASCADE, чтобы удалить 
все заказы связанные с удаленным клиентом. 

- В cost модели Order я использовал поле с фиксированной точностью с восемью цифрами и 
двумя знаками после запятой (8, 2). 
- После внесения изменений в модели, вам необходимо выполнить миграцию 
(python manage.py makemigrations и python manage.py migrate), чтобы изменения отразились в базе данных.
'''

'''
В этом примере у модели Salary есть поле employee, которое устанавливает связь один к одному с моделью Employee. 
То есть каждая запись в модели Salary будет иметь только одну связанную запись в модели Employee.
Также есть поле salary_amount, которое хранит значение заработной платы для данного сотрудника.
нужно выполнить миграцию после создания моделей с помощью команды  python manage.py makemigrations и python manage.py migrate для применения изменений в базе данных.
'''
