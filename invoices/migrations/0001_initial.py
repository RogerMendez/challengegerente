# Generated by Django 4.0.6 on 2022-07-07 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reservations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time registered in created at', verbose_name='Created ad')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time registeres in modified at', verbose_name='Modified at')),
                ('business_name', models.CharField(max_length=100)),
                ('nit', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('total', models.FloatField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('reservation', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='reservations.reservation')),
            ],
            options={
                'verbose_name': 'Factura',
                'verbose_name_plural': 'Facturas',
                'ordering': ['date'],
            },
        ),
    ]
