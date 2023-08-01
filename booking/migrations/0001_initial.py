# Generated by Django 4.2.2 on 2023-06-23 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nombre')),
                ('lastname', models.CharField(max_length=200, verbose_name='Apellidos')),
                ('phone', models.TextField(max_length=100, verbose_name='Nombre')),
                ('mail', models.EmailField(max_length=200, verbose_name='Correo')),
                ('contry', models.CharField(max_length=200, verbose_name='Pais')),
                ('city', models.CharField(max_length=200, verbose_name='Ciudad')),
                ('hotel', models.CharField(max_length=200, verbose_name='Hotel')),
                ('tour', models.CharField(max_length=200, verbose_name='Tours')),
                ('adults', models.CharField(max_length=100, verbose_name='Adultos')),
                ('childre', models.CharField(max_length=100, verbose_name='Niños')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado el')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Editado el')),
            ],
        ),
    ]
