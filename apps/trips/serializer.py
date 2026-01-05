from rest_framework import serializers

from apps.trips.models import Trip, Stop
from apps.customers.serializer import CustomerSerializer
from apps.vehicles.serializer import VehicleSerializer
from apps.drivers.serializer import DriverProfileSerializer

class StopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stop
        fields = ['id', 'location', 'stop_order']
        read_only_field = ['id']

class TripListSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    vehicle = VehicleSerializer()
    driver = DriverProfileSerializer()

    class Meta:
        model = Trip
        fields = [
            'id',
            'customer',
            'vehicle',
            'driver',
            'status',
            'start_date',
            'end_date',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']