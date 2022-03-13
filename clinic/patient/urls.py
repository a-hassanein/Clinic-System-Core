from django.urls import include, path
from rest_framework import routers
from .views import *
router = routers.DefaultRouter()
router.register(r'patient' , PatientViewset )
urlpatterns = [
     path('info/<id>', getPatient),
     path('myappointment/<id>', getPatientAppointment),
     path('prescriptionList/<id>', prescriptionList),
     path('labList/<id>', labList),
     path('', include(router.urls)),
     path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]