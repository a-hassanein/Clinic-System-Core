from django.shortcuts import render
from rest_framework import viewsets
from .models import FavDrugs 
from .serializers import FavDrugSerializer

# Create your views here.

class FavDrugViewset(viewsets.ModelViewSet):
    queryset = FavDrugs.objects.all()
    serializer_class = FavDrugSerializer

