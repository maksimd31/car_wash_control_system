# Generated by Django 4.2.4 on 2023-09-01 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_wash', '0003_alter_order_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additionalservice',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
