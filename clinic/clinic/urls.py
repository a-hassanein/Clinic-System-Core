"""clinic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
#from appointment.urls import router
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('appointment/' , include('appointment.urls')),
    path('prescription/', include('prescription.urls')),
    path('patient/', include('patient.urls')),
    path('labs/', include('labs.urls')),
    path('surgery/', include('surgery.urls')),
    path('bill/', include('bill.urls')),
    path('clinic/', include('doctor_clinic.urls')),
    path('materials/', include('materials.urls')),
    path('assistant/', include('assistant.urls')),
    path('doctors/', include('doctors.urls')),
    path('favlabs/', include('labfav.urls')),
]

