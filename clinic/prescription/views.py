from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.decorators import api_view
from main.models import Prescription
from .serializers import PrescriptionSerializer
from rest_framework import status

# Create your views here.

@api_view(['GET', 'POST'])
def drugs_list(request):
    if request.method == 'GET':
        drugs = Prescription.objects.all()
        serializer = PrescriptionSerializer(drugs, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = PrescriptionSerializer(data=request.data)
        if serializer.is_valid:
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def drug_list(request,id):
    pass
