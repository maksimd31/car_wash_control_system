from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from .models import Client, Order
from .forms import ClientForm, ClientUpdateForm, OrderForm


# CLIENT
# filename views.py
def add_client(request):
    """
    Создание клиента
    :param request: ответ на запрос GET
    :return: render 'add_client.html'
    """
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')  # Перенаправление на страницу со списком клиентов
    else:
        form = ClientForm()

    context = {'form': form}
    return render(request, 'add_client.html', context)


# filename views.py
def delete_client(request):
    """
    Удаление пользователей
    :param request: ответ на запрос GET
    :return: render(request, 'delete_client.html')
    """
    if request.method == 'POST':
        license_plate = request.POST.get('license_plate')
        try:
            client = Client.objects.get(license_plate=license_plate)
            client.delete()
            return redirect('client_list')
        except Client.DoesNotExist:
            error_message = 'Клиент с указанным государственным номером не найден.'
            return render(request, 'delete_client.html', {'error_message': error_message})

    return render(request, 'delete_client.html')


# filename views.py
def update_client(request, license_plate):
    """
    Редактирование Пользователей
    :param request: ответ на запрос GET
    :param license_plate:
    :return: render(request, 'update_client.html'
    """
    client = get_object_or_404(Client, license_plate=license_plate)

    if request.method == 'POST':
        form = ClientUpdateForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client_detail', license_plate=license_plate)
    else:
        form = ClientUpdateForm(instance=client)

    return render(request, 'update_client.html', {'form': form, 'client': client})


# ORDER
# filename views.py
def create_order(request):
    """
    Создание заказа, сделки
    :param request: ответ на запрос GET
    :return: return render(request, 'create_order.html'
    """
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm()
    return render(request, 'create_order.html', {'form': form})


# filename views.py
def delete_order(request, order_id):
    """
    Удаление заказа/сделки
    :param request: ответ на запрос GET
    :param order_id: идентификатор заказа/сделки
    :return: render(request, 'delete_order.html'
    """
    order = get_object_or_404(Order, pk=order_id)
    # Здесь мы используем функцию get_object_or_404,
    # чтобы получить объект модели Order по его первичному ключу (pk).
    # Если заказ с указанным order_id не существует, будет сгенерирована страница ошибки HTTP 404.
    if request.method == 'POST':
        order.delete()
        return redirect('order_list')
    #     Здесь мы проверяем, был ли отправлен POST-запрос.
    #     Если это так, то мы удаляем заказ, вызывая метод delete() для объекта order.
    #     Затем мы перенаправляем пользователя на страницу, которая отображает список заказов
    #     (в данном случае с именем order_list).

    return render(request, 'delete_order.html', {'order': order})


# filename views.py
def update_order(request, order_id):
    """
    Редактирование заказа/сделки
    :param request: ответ на запрос GET
    :param order_id: идентификатор заказа/сделки
    :return: render(request, 'update_order.html'
    """
    order = get_object_or_404(Order, pk=order_id)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm(instance=order)

    return render(request, 'update_order.html', {'form': form, 'order': order})


def order_list(request):
    """
    отображает список заказов (в данном случае с именем order_list).
    :param request:
    :return:  render(request, 'order_list.html'
    """
    orders = Order.objects.all()
    return render(request, 'order_list.html', {'orders': orders})


"""
Здесь мы определяем функции для каждой операции: create_order, delete_order, update_order и order_list.
- create_order: Создает новый заказ. Если запрос методом POST, то создается экземпляр формы (OrderForm) с данными из запроса и, если форма действительна, то сохраняется новый заказ в базу данных и происходит перенаправление на страницу списка заказов.
- delete_order: Удаляет существующий заказ. Если запрос методом POST, то заказ удаляется из базы данных и происходит перенаправление на страницу списка заказов.
- update_order: Редактирует существующий заказ. Если запрос методом POST, то создается экземпляр формы (OrderForm) с данными из запроса и, если форма действительна, то сохраняются изменения заказа в базе данных и происходит перенаправление на страницу списка заказов.
- order_list: Отображает список всех заказов.
Наконец, нужно создать соответствующие HTML-шаблоны для каждой из этих функций: create_order.html, delete_order.html, update_order.html и order_list.html, чтобы отображать формы и список заказов.
Также понадобится обновить файл urls.py, чтобы добавить соответствующие маршруты для этих функций.
"""


def page_not_found(reqwest, exception):
    """
    Функция предоставления несуществующей страницы
    :param reqwest:
    :param exception:
    :return:
    """
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
