from enum import Enum
from django.db import models
from datetime import datetime


# class FuelType(Enum):
#     PETROL = 'Petrol'
#     EV = 'Electric Vehicle'
#     DIESEL = 'Diesel'
    
class Brand(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name  

    

class Vehicle(models.Model):
    vehicle_name = models.CharField(max_length=100)
    vehicle_brand = models.ForeignKey(Brand, on_delete=models.CASCADE)  
    
    def __str__(self):
        return self.vehicle_name  
