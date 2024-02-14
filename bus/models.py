from django.db import models
from bus_auth.models import Users

# Model to store bus information
class Bus(models.Model):
    bus_id = models.AutoField(primary_key=True)
    bus_name = models.CharField(max_length=50)
    bus_number = models.CharField(max_length=10)
    bus_capacity = models.IntegerField()
    bus_fare = models.IntegerField()

    def __str__(self):
        return self.bus_name

# Model to store stations
class Station(models.Model):
    station_id = models.AutoField(primary_key=True)
    station_name = models.CharField(max_length=50)


# Model to store bus schedule
class BusSchedule(models.Model):
    schedule_id = models.IntegerField()
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    schedule_date = models.DateField()
    schedule_time = models.TimeField()
    station = models.ForeignKey(Station, on_delete=models.CASCADE)


# Model to store bus booking
class BusBooking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    schedule = models.ForeignKey(BusSchedule, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    booking_date = models.DateField()
