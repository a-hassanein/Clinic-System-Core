from django.shortcuts import render
from main.models import Contactus
from .serializers import ContactusSerializer
from rest_framework import viewsets

# Create your views here.

class ContactusViewset(viewsets.ModelViewSet):
    queryset = Contactus.objects.all()
    serializer_class = ContactusSerializer
