from django.shortcuts import render
from rest_framework import viewsets
from main.models import Clinic
from .serializers import ClinicSerializer

# Create your views here.

class Clinic_DoctorViewset(viewsets.ModelViewSet):
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer