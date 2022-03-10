from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from main.models import Bill
from .serializers import BillSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

# class BillViewset(viewsets.ModelViewSet):
#     queryset = Bill.objects.all()
#     serializer_class = BillSerializer



@api_view(['GET'])
def BillGet(requset,id):

    bill = Bill.objects.filter(appointment_id=id)
    print(bill[0].activity_name)

    if(requset.method == 'GET'):
        billData = []
        for i in range(len(bill)):
            response = BillSerializer(bill[i])
            billData.append(response.data)
        return Response(billData)

@api_view(['POST'])
def BillPost(requset):

    if requset.method == "POST":
        data = requset.data
        serializer = BillSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

