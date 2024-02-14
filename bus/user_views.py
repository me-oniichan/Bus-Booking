from django.contrib.auth.decorators import login_required
from django.db import connection
from django.shortcuts import render
from bus.models import Bus, Station

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
