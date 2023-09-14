# filename add_random_client
from car_wash.models import Client
from faker import Faker
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Заполнить таблицу Client данными'

    def handle(self, *args, **options):
        fake = Faker('ru_RU')

        for _ in range(100):
            license_plate = fake.license_plate()
            full_name = fake.name()
            phone_number = fake.phone_number()
            car_model = fake.car_model()

            client = Client(
                license_plate=license_plate,
                full_name=full_name,
                phone_number=phone_number,
                car_model=car_model
            )
            client.save()

        self.stdout.write(self.style.SUCCESS('Успешно заполнена таблица клиенты со случайными данными'))
