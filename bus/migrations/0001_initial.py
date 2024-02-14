# Generated by Django 5.0.2 on 2024-02-14 07:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('bus_id', models.AutoField(primary_key=True, serialize=False)),
                ('bus_name', models.CharField(max_length=50)),
                ('bus_number', models.CharField(max_length=10)),
                ('bus_capacity', models.IntegerField()),
                ('bus_fare', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('station_id', models.AutoField(primary_key=True, serialize=False)),
                ('station_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='BusSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schedule_id', models.IntegerField()),
                ('schedule_date', models.DateField()),
                ('schedule_time', models.TimeField()),
                ('bus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bus.bus')),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bus.station')),
            ],
        ),
        migrations.CreateModel(
            name='BusBooking',
            fields=[
                ('booking_id', models.AutoField(primary_key=True, serialize=False)),
                ('booking_date', models.DateField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bus.busschedule')),
            ],
        ),
    ]