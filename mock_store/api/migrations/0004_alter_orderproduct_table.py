# Generated by Django 4.0 on 2022-01-01 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_orderproduct_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='orderproduct',
            table='api_order_products',
        ),
    ]
