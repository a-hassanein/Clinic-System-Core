from django.shortcuts import render
from main.models import Assistant
from .serializers import AssistantSerializer
from rest_framework import viewsets

# Create your views here.

class AssistantViewset(viewsets.ModelViewSet):
    queryset = Assistant.objects.all()
    serializer_class = AssistantSerializer