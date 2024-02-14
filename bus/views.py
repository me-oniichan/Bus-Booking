from django.forms import formset_factory
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from bus.forms import BusForm, ScheduleForm
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotFound
from bus.models import Bus, BusSchedule
import random

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

def create_route(request):
    '''Create a new route for a bus'''
    if(request.user.is_superuser):
        if request.method == 'POST':
            form = formset_factory(ScheduleForm)
            forms = form(request.POST)
            sid = random.randint(1, 100000)
            bus = Bus.objects.get(bus_id = int(request.POST["bus_id"]))
            if forms.is_valid():
                for form in forms:
                    schedule = BusSchedule(schedule_id=sid, bus=bus, schedule_date=form.cleaned_data['schedule_date'], schedule_time=form.cleaned_data['schedule_time'], station=form.cleaned_data['station'])
                    schedule.save()
            return redirect('/bus/bus_list')
        else:
            return HttpResponseBadRequest();
    else:
        return HttpResponseBadRequest();

def show_route(request, bus_id):
    '''Show the route of a bus'''
    try:
        bus = Bus.objects.get(bus_id=bus_id)
        route_ids = BusSchedule.objects.filter(bus=bus)
        return render(request, 'show_route.html', {'routes': route_ids, 'is_superuser': request.user.is_superuser, 'bus_id': bus_id, "forms": formset_factory(ScheduleForm, extra=1)})
    except Bus.DoesNotExist:
        return HttpResponseNotFound();

def bus_list(request):
    '''List all the buses'''
    buses = Bus.objects.all()
    return render(request, 'bus_list.html', {'buses': buses, 'is_superuser': request.user.is_superuser})

def delete_bus(request):
    '''Delete a bus'''
    if(request.user.is_superuser and request.method == "POST"):
        try:
            bus = Bus.objects.get(bus_id=int(request.POST["bus_id"]))
            bus.delete()
            return redirect('/bus/bus_list')
        except Bus.DoesNotExist:
            return HttpResponseNotFound();
    else:
        return HttpResponseBadRequest();


