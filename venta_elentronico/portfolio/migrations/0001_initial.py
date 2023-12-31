# Generated by Django 4.2.2 on 2023-07-25 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Titulo')),
                ('description', models.TextField(verbose_name='Descricion')),
                ('image', models.ImageField(upload_to='', verbose_name='Imagen')),
                ('create', models.DateTimeField(auto_now_add=True, verbose_name='fecha de creacion ')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='fecha de  edicion')),
            ],
            options={
                'verbose_name': 'proyecto',
                'verbose_name_plural': 'proyectos',
                'ordering': ['-create'],
            },
        ),
    ]
