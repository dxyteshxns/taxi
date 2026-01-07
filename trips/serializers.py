from rest_framework import serializers
from .models import Trip
from drivers.serializers import DriverProfileSerializer
from vehicles.serializers import VehicleSerializer

class TripSerializer(serializers.ModelSerializer):
    driver = DriverProfileSerializer(read_only=True)
    vehicle = VehicleSerializer(read_only=True)

    class Meta:
        model = Trip
        fields = '__all__'
 
