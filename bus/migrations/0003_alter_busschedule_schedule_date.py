# Generated by Django 5.0.2 on 2024-02-14 09:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bus', '0002_weeks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='busschedule',
            name='schedule_date',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bus.weeks'),
        ),
    ]
