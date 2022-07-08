# Generated by Django 4.0.6 on 2022-07-07 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time registered in created at', verbose_name='Created ad')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time registeres in modified at', verbose_name='Modified at')),
                ('total', models.FloatField()),
                ('check_in', models.DateTimeField()),
                ('check_out', models.DateTimeField()),
                ('state_reservation', models.CharField(choices=[('Pendiente', 'Pendiente'), ('Pagado', 'Pagado'), ('Eliminado', 'Eliminado')], max_length=20)),
            ],
            options={
                'verbose_name': 'Reservación',
                'verbose_name_plural': 'Reservaciones',
                'ordering': ['check_in', 'check_out'],
            },
        ),
    ]