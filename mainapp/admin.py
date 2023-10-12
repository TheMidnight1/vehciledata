from django.contrib import admin
from .models import Vehicle,Brand
# Register your models here.
admin.site.register([Brand,Vehicle])
