from django.shortcuts import render
from rest_framework import viewsets
from labfav.models import FavLabs, FavScans
from .serializers import FavBillSerializer, FavScanSerializer

# Create your views here.

class FavBillViewset(viewsets.ModelViewSet):
    queryset = FavLabs.objects.all()
    serializer_class = FavBillSerializer

class FavScanViewset(viewsets.ModelViewSet):
    queryset = FavScans.objects.all()
    serializer_class = FavScanSerializer