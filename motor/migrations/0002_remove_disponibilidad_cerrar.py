# Generated by Django 4.2.1 on 2023-08-01 02:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('motor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='disponibilidad',
            name='cerrar',
        ),
    ]
