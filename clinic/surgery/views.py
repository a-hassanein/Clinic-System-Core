from django.shortcuts import render
from rest_framework import viewsets
from main.models import Surgery
from .serializers import SurgerySerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class SurgeryViewset(viewsets.ModelViewSet):
    queryset = Surgery.objects.all()
    serializer_class = SurgerySerializer
    permission_classes = [IsAuthenticated]

