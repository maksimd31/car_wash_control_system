from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

from car_wash.models import Client


class Command(BaseCommand):
    help = 'Заполнить таблицу Client данными'

    def handle(self, *args, **kwargs):
        for _ in range(10):
            license_plate = get_random_string(10)
            full_name = get_random_string(10)
            phone_number = get_random_string(10)
            car_model = get_random_string(10)
            Client.objects.create(license_plate=license_plate, full_name=full_name, phone_number=phone_number,
                                  car_model=car_model)
