# Generated by Django 3.1.3 on 2021-01-06 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Travelling', '0009_auto_20210106_2217'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='passengerdata',
            name='charge',
        ),
    ]
