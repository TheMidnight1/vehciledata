from django import forms
from .models import Brand, Vehicle

class VehicleForm(forms.Form):
    brand = forms.ModelChoiceField(queryset=Brand.objects.all(), empty_label=None)
    vehicle = forms.ModelChoiceField(queryset=Vehicle.objects.none(), empty_label=None)
