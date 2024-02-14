from django.forms import ModelForm, widgets
from .models import Bus, BusSchedule, Station
from django.db import models
from django import forms

class BusForm(ModelForm):
    class Meta:
        model = Bus
        fields = ['bus_name', 'bus_number', 'bus_capacity', 'bus_fare']


class ScheduleForm(ModelForm):
    class Meta:
        model = BusSchedule
        fields = ['schedule_date', 'schedule_time', 'station']

        widgets = {
            'schedule_time': widgets.TimeInput(attrs={'type': 'time'}),
        }

        label = {
            'schedule_date': 'week_name',
        }
