# Generated by Django 4.2.1 on 2023-05-18 21:02

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Titulo')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Descripcion')),
                ('image', models.ImageField(default='null', upload_to='rooms', verbose_name='Imagen')),
                ('cash', models.CharField(max_length=100, verbose_name='Precios')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado')),
            ],
            options={
                'verbose_name': 'Habitacion',
                'verbose_name_plural': 'Habitaciones',
            },
        ),
    ]
