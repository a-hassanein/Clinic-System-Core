from django.shortcuts import render
from main.models import Labs 
from .serializers import LabsSerializer
from rest_framework import viewsets

# Create your views here.


class LabsViewset(viewsets.ModelViewSet):
    queryset = Labs.objects.all()
    serializer_class = LabsSerializer


