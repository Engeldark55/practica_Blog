# Generated by Django 3.2 on 2021-04-10 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255, verbose_name='nombre del autor')),
                ('apellidos', models.CharField(max_length=300, verbose_name='apellidos del autor')),
                ('facebook', models.URLField(blank=True, null=True, verbose_name='facebook')),
                ('email', models.EmailField(max_length=254, verbose_name='correo del autor')),
                ('estado', models.BooleanField(default=True, verbose_name='autor activo/no activo')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='fecha de creacion autor')),
            ],
            options={
                'verbose_name': 'autor',
                'verbose_name_plural': 'autores',
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre de categoria')),
                ('estado', models.BooleanField(default=True, verbose_name='Categoria activada/categoria no activada')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de creacion categoria')),
            ],
            options={
                'verbose_name': 'categoria',
                'verbose_name_plural': 'categorias',
            },
        ),
    ]
