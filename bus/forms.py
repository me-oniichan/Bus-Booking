from django.forms import ModelForm
from .models import Bus

class BusForm(ModelForm):
    class Meta:
        model = Bus
        fields = ['bus_name', 'bus_number', 'bus_capacity', 'bus_fare']
