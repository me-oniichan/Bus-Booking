from django.contrib.auth.decorators import login_required
from django.db import connection
from django.http.response import HttpResponseBadRequest
from django.shortcuts import redirect, render
import bus
from bus.models import Bus, BusBooking, Station

@login_required
def dashboard(request):
    if request.method == 'POST':
        source = Station.objects.get(station_id= int(request.POST['source_id']))
        destination = Station.objects.get(station_id= int(request.POST['destination_id']))
        
        query = 'SELECT source.bus_id FROM bus_busschedule source join bus_busschedule dest on source.schedule_id = dest.schedule_id where source.schedule_time < dest.schedule_time and source.station_id = %s and dest.station_id = %s'
        
        stations = Station.objects.all()
        with connection.cursor() as cursor:
            cursor.execute(query, [source.station_id, destination.station_id])
            results = cursor.fetchall()
            results = [item[0] for item in results]
            # use resulting primary key to extract Bus 
            buses = Bus.objects.filter(bus_id__in=results) 
            return render(request, "dashboard.html",{
                'stations': stations,
                'buses': buses
            })

    stations = Station.objects.all()
    buses = Bus.objects.all()
    return render(request, "dashboard.html",{
        'stations': stations,
        'buses': buses
    })


def bus_details(request, bus_id):
    bus = Bus.objects.get(bus_id=bus_id)
    return render(request, "bus_details.html",{
        'bus': bus,
        'row1': range(1, bus.bus_capacity+1, 4),
        "row2": range(2, bus.bus_capacity+1, 4),
        "row3": range(3, bus.bus_capacity+1, 4),
        "row4": range(4, bus.bus_capacity+1, 4)
    })

@login_required
def book_bus(request):
    if request.method == 'POST':
        bus = Bus.objects.get(bus_id= int(request.POST['bus_id']))
        seat_number = int(request.POST['seat_num'])
        print(seat_number)
        record = BusBooking.objects.create(
            user_id=request.user,
            bus_id=bus,
            seat_number=seat_number
        )
        record.save()
        return redirect('/bus/bus_details/'+str(bus.bus_id))
    return HttpResponseBadRequest()
