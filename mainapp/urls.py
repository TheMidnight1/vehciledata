from django.contrib import admin
from django.urls import path,include
from mainapp.views import vehicle_selection,get_vehicles

app_name = "mainapp"
urlpatterns = [
    path('',vehicle_selection),
    path('get_vehicles/<int:brand_id>/', get_vehicles, name='get_vehicles')

    
]