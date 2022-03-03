import django


from django.urls import path
from . import views


urlpatterns = [
    path('drugs', views.drugs_list, name='drugs_list'),
    
]