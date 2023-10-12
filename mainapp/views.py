from django.shortcuts import render
from .models import Vehicle
from .forms import VehicleForm
from django.http import JsonResponse

def get_vehicles(request, brand_id):
    vehicles = Vehicle.objects.filter(vehicle_brand_id=brand_id).values('id', 'vehicle_name')
    return JsonResponse(list(vehicles), safe=False)


def vehicle_selection(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            selected_vehicle = form.cleaned_data['vehicle']
            # Do something with the selected vehicle
    else:
        form = VehicleForm()
    return render(request, 'form.html', {'form': form})

