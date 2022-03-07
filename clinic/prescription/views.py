from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.decorators import api_view
from main.models import Prescription
from .serializers import PrescriptionSerializer
from rest_framework import status, viewsets

# Create your views here.

class Prescriptionviewset(viewsets.ModelViewSet):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer
