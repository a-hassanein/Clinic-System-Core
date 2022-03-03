from django.shortcuts import render
from rest_framework import viewsets
from main.models import Bill
from .serializers import BillSerializer

# Create your views here.

class BillViewset(viewsets.ModelViewSet):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
