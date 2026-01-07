"""
URL configuration for taxi_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from accounts.views import UserViewSet
from drivers.views import DriverProfileViewSet
from vehicles.views import VehicleViewSet
from trips.views import TripViewSet, trips_list, trip_detail
from payments.views import PaymentViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'drivers', DriverProfileViewSet)
router.register(r'vehicles', VehicleViewSet)
router.register(r'trips', TripViewSet)
router.register(r'payments', PaymentViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('trips/', trips_list, name='trips_list'),
    path('trips/<int:pk>/', trip_detail, name='trip_detail'),
]


