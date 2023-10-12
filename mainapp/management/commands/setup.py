import os
import json
from django.core.management.base import BaseCommand
from django.core.management import call_command
from mainapp.models import Brand,Vehicle



class Command(BaseCommand):
    help = "Setup brands and vehicles data"


    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING("Setting up applications..."))
        call_command('makemigrations', interactive=False)
        call_command('migrate', interactive=False)
        
        
        self.stdout.write(self.style.WARNING("Flushing `Brand` & `Vehcile`..."))
        Vehicle.objects.all().delete()
        Brand.objects.all().delete()
        
        with open(os.path.join("mainapp","management","dataset.json"),"r") as file:
            data = json.load(file)
            file.close()

            brand_list = [Brand(name=brand) for brand in data]
            saved_brands = Brand.objects.bulk_create(brand_list)
            self.stdout.write(self.style.WARNING(f"{len(saved_brands)} brand(s) were saved!"))
            brand_dict = {brand.name: brand.pk for brand in saved_brands}
            
            vehicle_list = []
            for brand,vehicles in data.items():
                for vehicle_name in vehicles:
                        vehicle_brand_pk= brand_dict.get(brand)
                        
                        if vehicle_brand_pk:
                            vehicle_list.append(Vehicle(vehicle_name=vehicle_name,vehicle_brand = Brand(pk=vehicle_brand_pk)))
            
            saved_vehicle = Vehicle.objects.bulk_create(vehicle_list)
            self.stdout.write(self.style.WARNING(f"{len(saved_vehicle)} vehicle(s) were saved!"))
            

            self.stdout.write(self.style.SUCCESS("Successfully loaded data for `brands` & `vehciles`."))
        
        
        
    
        
