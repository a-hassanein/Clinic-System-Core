from django.shortcuts import render
from main.models import Material
from .serializers import MaterialsSerializer
from rest_framework import viewsets

# Create your views here.

class MaterialsViewset(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialsSerializer


