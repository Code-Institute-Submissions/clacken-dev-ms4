# Generated by Django 3.2.9 on 2021-12-11 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_rename_price_order_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='email',
        ),
    ]
