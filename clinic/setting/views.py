from django.shortcuts import render
from main.models import Assistant
from .serializers import SettingSerializer
from rest_framework import viewsets

# Create your views here.

class SettingViewset(viewsets.ModelViewSet):
    queryset = Assistant.objects.all()
    serializer_class = SettingSerializer