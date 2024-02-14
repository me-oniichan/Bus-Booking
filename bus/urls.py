#initite django urls file
from django.urls import path
from . import views

urlpatterns = [
    path('add_bus/', views.add_bus, name='add_bus'),
    path('bus_list/', views.bus_list, name='bus_list'),
    path('bus_route', views.create_route, name='bus_route'),
    path('show_route/<int:bus_id>/', views.show_route, name='show_route'),
]
