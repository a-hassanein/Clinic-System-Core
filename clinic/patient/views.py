from django.shortcuts import render
from main.models import Patient , Appointment ,Prescription ,Labs
from .serializers import PatientSerializer
from appointment.serializers import AppointmentSerializer
from prescription.serializers import PrescriptionSerializer
from labs.serializers import LabsSerializer
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.


class PatientViewset(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

@api_view(['GET'])
def getPatient(request, id):
    patient=Patient.objects.get(patient_id=id)
    print('++++++++++++++++++++++++++++',patient)

    if request.method == 'GET':
        serializer = PatientSerializer(patient)
        return Response(serializer.data)


@api_view(['GET'])
def getPatientAppointment(request, id):
    appointment=Appointment.objects.filter(patient_id=id)
    print('=========================',appointment)

    if request.method == 'GET':
        Appdata=[]
        for i in range(len(appointment)):
            serializer = AppointmentSerializer(appointment[i])
            Appdata.append(serializer.data)
        return Response(Appdata) 

    
@api_view(['GET'])
def prescriptionList(request, id):
    presc=Prescription.objects.filter(appointment_id=id)
    print(presc[0])

    if request.method == 'GET':
        prescdata=[]
        for i in range(len(presc)):
            serializer = PrescriptionSerializer(presc[i])
            prescdata.append(serializer.data)
        return Response(prescdata)

@api_view(['GET'])
def labList(request, id):
    labs=Labs.objects.filter(appointment_id=id)
    print(labs[0])

    if request.method == 'GET':
        labdata=[]
        for i in range(len(labs)):
            serializer = LabsSerializer(labs[i])
            labdata.append(serializer.data)
        return Response(labdata)

