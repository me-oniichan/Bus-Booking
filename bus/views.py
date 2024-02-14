from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from bus.forms import BusForm
from bus.models import Bus
from django.http import HttpResponse

@login_required
def add_bus(request) -> HttpResponse:
    '''Add a new bus to the database'''
    if(request.user.is_superuser):
        if request.method == 'POST':
            form = BusForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('bus_list')
        else:
            form = BusForm()
        return render(request, 'add_bus.html', {'form': form})

def bus_create_route(request):
    '''Create a new route for a bus'''
    if(request.user.is_superuser):
        if request.method == 'POST':
            form = RouteForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('bus_list')
        else:
            form = RouteForm()
        return render(request, 'create_route.html', {'form': form})

