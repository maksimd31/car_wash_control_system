# Generated by Django 4.2.4 on 2023-09-01 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_wash', '0002_additionalservice_remove_order_comment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
