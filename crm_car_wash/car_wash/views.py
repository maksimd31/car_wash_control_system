from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .models import Client, Order, Employee

def new_order(request):
    if request.method == "POST":
        car_number = request.POST.get('car_number')
        client = Client.objects.filter(car_number=car_number).first()
        if client:
            # Клиент с таким номером есть в базе данных
            orders = Order.objects.filter(client=client)
            return render(request, 'order_confirm.html', {'client': client, 'orders': orders})
        else:
            # Открываем форму добавления нового клиента
            return render(request, 'add_client.html', {'car_number': car_number})
    return render(request, 'new_order.html')

def add_client(request):
    if request.method == "POST":
        car_number = request.POST.get('car_number')
        name = request.POST.get('name')
        # Создаем нового клиента и сохраняем в базу данных
        client = Client(car_number=car_number, name=name)
        client.save()
        return redirect('new_order')
    return render(request, 'add_client.html')

def calculate_price(request):
    if request.method == "POST":
        wash_type = request.POST.get('wash_type')
        car_class = request.POST.get('car_class')
        vacuum = request.POST.get('vacuum')
        additional_services = request.POST.getlist('additional_services')
        employee_id = int(request.POST.get('employee'))

        wash_prices = {'body_carpet': 500, 'complex': 1000, 'standard': 700}
        vacuum_prices = {'interior': 150, 'trunk': 50, 'both': 200}
        car_class_prices = {1: 100, 2: 200, 3: 300}

        total_price = wash_prices[wash_type]
        total_price += vacuum_prices[vacuum]
        total_price += car_class_prices[int(car_class)]

        for service in additional_services:
            # Добавляем стоимость дополнительных услуг к общей цене
            # Дополнительные услуги и их цены могут храниться в отдельной модели
            total_price += service.price

        employee = Employee.objects.get(id=employee_id)
        # Начисляем 20% от стоимости общего чека
        employee.salary += total_price * 0.2
        employee.save()

        # Записываем данные заказа в таблицу Order
        client = Client.objects.get(car_number=request.POST.get('car_number'))
        order = Order(client=client, wash_type=wash_type, car_class=car_class, vacuum=vacuum)
        order.save()

        return render(request, 'final_price.html', {'total_price': total_price})
    return redirect('new_order')



