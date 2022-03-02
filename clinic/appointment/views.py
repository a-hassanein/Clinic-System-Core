from django.shortcuts import render
from rest_framework import viewsets
from main.models import Appointment
from .serializers import AppointmentSerializer

# Create your views here.

class AppointmentViewset(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer



