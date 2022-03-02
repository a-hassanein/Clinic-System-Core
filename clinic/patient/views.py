from django.shortcuts import render
from main.models import Patient 
from .serializers import PatientSerializer
from rest_framework import viewsets

# Create your views here.


class PatientViewset(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


