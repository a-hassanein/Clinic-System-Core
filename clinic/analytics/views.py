from django.shortcuts import render
from rest_framework.decorators import api_view

from analytics.models import Data
from analytics.serilizers import AnalyticSerializer
from appointment.serializers import AppointmentSerializer
from main.models import Appointment
from rest_framework.response import Response


import datetime

# Create your views here.


@api_view(['GET', 'POST'])
def getAnalytics(requset):

    if requset.method == 'GET':
        #data = Data.objects.all()
        appoiment = Appointment.objects.all()
        # for i in appoiment:
        #     print("Appoiment ---------------------------------------------->>>>>", i.appointment_date.month)
        datalist = []
        for i in appoiment:
            appoiment_month = i.appointment_date.month
            datalist.append(appoiment_month)

        print(datalist)

        serializer = AnalyticSerializer(data=datalist)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(datalist, status=200)

        # return Response(datalist)






    # bill = data.objects.all
    # print(bill[0].activity_name)

    # if(requset.method == 'GET'):
    #     billData = []
    #     for i in range(len(bill)):
    #         response = BillSerializer(bill[i])
    #         billData.append(response.data)
    #     return Response(billData)

# @api_view(['POST'])
# def BillPost(requset):

#     if requset.method == "POST":
#         data = requset.data
#         serializer = BillSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)
