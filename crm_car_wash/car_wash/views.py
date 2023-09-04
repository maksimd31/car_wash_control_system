from django.shortcuts import render, get_object_or_404
from .models import Client

def create_new_client(request):
    if request.method == 'POST':
        license_plate = request.POST.get('license_plate')
        client = get_object_or_404(Client, license_plate=license_plate)

        if client:
            # Клиент уже существует, добавляем данные
            client.full_name = request.POST.get('full_name')
            client.phone_number = request.POST.get('phone_number')
            client.car_model = request.POST.get('car_model')
            client.save()
            message = f"Данные клиента {client.full_name} обновлены успешно!"
        else:
            # Создаем нового клиента
            full_name = request.POST.get('full_name')
            phone_number = request.POST.get('phone_number')
            car_model = request.POST.get('car_model')
            new_client = Client(license_plate=license_plate, full_name=full_name, phone_number=phone_number, car_model=car_model)
            new_client.save()
            message = f"Новый клиент {new_client.full_name} успешно создан!"

        return render(request, 'result.html', {'message': message})
    else:
        return render(request, 'create_new_client.html')
#
# В этой функции, при отправке POST запроса, мы получаем государственный номер (license_plate) из формы отправки. Затем мы пытаемся найти клиента по государственному номеру с помощью функции get_object_or_404. Если клиент уже существует, мы обновляем его данные. Если клиента нет в базе данных, мы создаем нового клиента и сохраняем его.
# После создания или обновления клиента, функция возвращает шаблон result.html с сообщением об успешном выполнении операции.
# Вы можете создать два шаблона: create_new_client.html, который содержит форму для ввода государственного номера, и result.html, который отображает сообщение о результате операции.
# Обратите внимание, что в этом примере я предполагаю, что у вас уже есть необходимая конфигурация проекта Django и настройки маршрутизации для этих функций.


