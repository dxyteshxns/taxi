from django.contrib import admin
from .models import Vehicle

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('driver', 'make', 'model', 'plate_number', 'year')
    search_fields = ('plate_number', 'driver__user__email', 'make', 'model')
