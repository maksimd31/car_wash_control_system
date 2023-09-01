from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .models import Client, Order, Employee

# def new_order(request):
#     if request.method == "POST":
#         car_number = request.POST.get('car_number')
#         client = Client.objects.filter(car_number=car_number).first()
#         if client:
#             # Клиент с таким номером есть в базе данных
#             orders = Order.objects.filter(client=client)
#             return render(request, 'order_confirm.html', {'client': client, 'orders': orders})
#         else:
#             # Открываем форму добавления нового клиента
#             return render(request, 'add_client.html', {'car_number': car_number})
#     return render(request, 'new_order.html')
#
# def add_client(request):
#     if request.method == "POST":
#         car_number = request.POST.get('car_number')
#         name = request.POST.get('name')
#         # Создаем нового клиента и сохраняем в базу данных
#         client = Client(car_number=car_number, name=name)
#         client.save()
#         return redirect('new_order')
#     return render(request, 'add_client.html')

# def calculate_price(request):
#     if request.method == "POST":
#         wash_type = request.POST.get('wash_type')
#         car_class = request.POST.get('car_class')
#         vacuum = request.POST.get('vacuum')
#         additional_services = request.POST.getlist('additional_services')
#         employee_id = str(request.POST.get('employee'))
#
#         wash_prices = {'body_carpet': 500, 'complex': 1000, 'standard': 700}
#         vacuum_prices = {'interior': 150, 'trunk': 50, 'both': 200}
#         car_class_prices = {1: 100, 2: 200, 3: 300}
#
#         total_price = wash_prices[wash_type]
#         total_price += vacuum_prices[vacuum]
#         total_price += car_class_prices[int(car_class)]
#
#         for service in additional_services:
#             # Добавляем стоимость дополнительных услуг к общей цене
#             # Дополнительные услуги и их цены могут храниться в отдельной модели
#             total_price += service.price
#
#         employee = Employee.objects.get(id=employee_id)
#         # Начисляем 20% от стоимости общего чека
#         employee.salary += total_price * 0.2
#         employee.save()
#
#         # Записываем данные заказа в таблицу Order
#         client = Client.objects.get(car_number=request.POST.get('car_number'))
#         order = Order(client=client, wash_type=wash_type, car_class=car_class, vacuum=vacuum)
#         order.save()
#
#         return render(request, 'final_price.html', {'total_price': total_price})
#     return redirect('new_order')


# def calculate_price(request, car_class=None, employee_id=None):
#     if request.method == "POST":
#
#         wash_type = request.POST.get('wash_type')
#         car_class = int(car_class) if car_class is not None else 0
#         vacuum = request.POST.get('vacuum')
#         additional_services = request.POST.getlist('additional_services')
#         employee_id = int(employee_id) if employee_id is not None else 0
#
#         wash_prices = {'body_carpet': 500, 'complex': 1000, 'standard': 700}
#         vacuum_prices = {'interior': 150, 'trunk': 50, 'both': 200}
#         car_class_prices = {1: 100, 2: 200, 3: 300}
#
#         total_price = wash_prices.get(wash_type, 0)
#         total_price += vacuum_prices.get(vacuum, 0)
#         total_price += car_class_prices.get(int(car_class), 0)
#
#         for service in additional_services:
#             # Допустим, что у дополнительной услуги есть поле с названием 'price'
#             # и его значение можно получить таким образом: service.price
#             # Если у вас есть отдельная модель для дополнительных услуг, то вы должны использовать соответствующий метод для получения цены.
#             total_price += service.price
#
#         employee = Employee.objects.get(id=employee_id)
#         employee.salary += total_price * 0.2
#         employee.save()
#
#         client = Client.objects.get(car_number=request.POST.get('car_number'))
#         order = Order(client=client, wash_type=wash_type, car_class=car_class, vacuum=vacuum)
#         order.save()
#
#         return render(request, 'final_price.html', {'total_price': total_price})
#     return redirect('new_order')
#
#
# def calculate_price2(request):
#     if request.method == "POST":
#         wash_types = {'body_carpet': 'Body & Carpet Wash', 'complex': 'Complex Wash', 'standard': 'Standard Wash'}
#         car_class_prices = {1: 100, 2: 200, 3: 300}
#         vacuum_types = {'interior': 'Interior', 'trunk': 'Trunk', 'both': 'Both'}
#
#         context = {
#             'wash_types': wash_types,
#             'car_classes': car_class_prices,
#             'vacuum_types': vacuum_types,
#             'additional_services': AdditionalService.objects.all(),
#             'employees': Employee.objects.all(),
#         }
#
#         return render(request, 'calculate_price.html', context)
#
#     return redirect('new_order')


# views.py

from django.shortcuts import render, redirect
from .models import Client, AdditionalService, Employee, Order


def new_client(request):
    if request.method == "POST":
        license_plate = request.POST.get("license_plate")

        try:
            client = Client.objects.get(license_plate=license_plate)
        except Client.DoesNotExist:
            return redirect('add_client', license_plate=license_plate)

        return redirect('calculate_price', client_id=client.id)

    return render(request, 'new_client.html')


def add_client(request, license_plate):
    if request.method == "POST":
        name = request.POST.get("name")

        client = Client.objects.create(license_plate=license_plate, name=name)
        return redirect('calculate_price', client_id=client.id)

    return render(request, 'add_client.html')


def calculate_price(request, client_id):
    client = Client.objects.get(id=client_id)

    if request.method == "POST":
        wash_type = request.POST.get("wash_type")
        car_class = request.POST.get("car_class")
        vacuum = request.POST.get("vacuum")
        additional_services = request.POST.getlist("additional_services")
        employee_id = request.POST.get("employee")

        additional_service_objects = AdditionalService.objects.filter(id__in=additional_services)
        employee = Employee.objects.get(id=employee_id)

        total_price = calculate_total_price(wash_type, car_class, vacuum, additional_service_objects)

        order = Order.objects.create(
            client=client,
            wash_type=wash_type,
            car_class=car_class,
            vacuum=vacuum,
            employee=employee,
            total_price=total_price
        )

        employee.salary += total_price  # Увеличение заработной платы сотрудника
        employee.save()

        return redirect('save_order', order_id=order.id)

    wash_types = {'body_carpet': 'Body & Carpet Wash', 'complex': 'Complex Wash', 'standard': 'Standard Wash'}
    car_class_prices = {1: 100, 2: 200, 3: 300}
    vacuum_types = {'interior': 'Interior', 'trunk': 'Trunk', 'both': 'Both'}
    additional_services = AdditionalService.objects.all()
    employees = Employee.objects.all()

    context = {
        'wash_types': wash_types,
        'car_classes': car_class_prices,
        'vacuum_types': vacuum_types,
        'additional_services': additional_services,
        'employees': employees,
        'client': client,
    }

    return render(request, 'calculate_price.html', context)


def save_order(request, order_id):
    order = Order.objects.get(id=order_id)
    return render(request, 'save_order.html', {'order': order})


def calculate_total_price(wash_type, car_class, vacuum, additional_services):
    total_price = 0

    # Расчет стоимости основных услуг
    wash_type_prices = {'body_carpet': 100, 'complex': 150, 'standard': 80}
    car_class_prices = {'1': 100, '2': 200, '3': 300}
    vacuum_prices = {'interior': 50, 'trunk': 30, 'both': 70}

    total_price += wash_type_prices.get(wash_type, 0)
    total_price += car_class_prices.get(car_class, 0)
    total_price += vacuum_prices.get(vacuum, 0)

    # Расчет стоимости дополнительных услуг
    for additional_service in additional_services:
        total_price += additional_service.price

    return total_price
