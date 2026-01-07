from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Trip
from .serializers import TripSerializer

class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

    @action(detail=True, methods=['post'])
    def accept(self, request, pk=None):
        trip = self.get_object()
        driver_profile = request.user.driverprofile  # предполагаем, что у пользователя есть DriverProfile

        if trip.status != 'requested':
            return Response({'detail': 'Trip already taken'}, status=status.HTTP_400_BAD_REQUEST)

        trip.driver = driver_profile
        trip.vehicle = driver_profile.vehicles.first()  # берём первую машину водителя
        trip.status = 'accepted'
        trip.save()

        return Response(self.get_serializer(trip).data)


def trips_list(request):
    trips = Trip.objects.all()
    return render(request, "trips_list.html", {"trips": trips})

def trip_detail(request, pk):
    trip = get_object_or_404(Trip, pk=pk)
    return render(request, "trip_detail.html", {"trip": trip})


