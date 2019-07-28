# Generated by Django 2.2.2 on 2019-07-25 14:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('organizador', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Almacen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ISBC', models.CharField(max_length=100, unique=True)),
                ('producto', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='proovedores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CUIIL', models.CharField(max_length=100, unique=True)),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.DecimalField(decimal_places=0, max_digits=100)),
            ],
        ),
        migrations.CreateModel(
            name='stock_entrada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proovedor', models.CharField(max_length=100, unique=True)),
                ('producto_entrante', models.CharField(max_length=100, unique=True)),
                ('cant_ingreso', models.DecimalField(decimal_places=0, max_digits=100)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='stock_salida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto_salida', models.CharField(max_length=100, unique=True)),
                ('cant_vendida', models.DecimalField(decimal_places=0, max_digits=100)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
