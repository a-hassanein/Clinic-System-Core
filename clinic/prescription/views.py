from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.decorators import api_view
from main.models import Prescription
from .serializers import PrescriptionSerializer
from rest_framework import status, viewsets

# Create your views here.

class Prescriptionviewset(viewsets.ModelViewSet):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer

@api_view(['GET'])
def drugget(request, id):
    drugs=Prescription.objects.filter(appointment_id=id)
    print(drugs[0])

    if request.method == 'GET':
        drugsdata=[]
        for i in range(len(drugs)):
            serializer = PrescriptionSerializer(drugs[i])
            drugsdata.append(serializer.data)
        return Response(drugsdata)


@api_view(['GET','DELEtE'])
def drugdelete(request,id):
    drug = Prescription.objects.get(prescription_id=id)
    if request.method == 'GET':
        serializer = PrescriptionSerializer(drug)
        return Response(serializer.data)
    if request.method == 'DELETE':
        drug.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)