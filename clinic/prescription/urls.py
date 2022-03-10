from django.urls import include, path
from rest_framework import routers
from .views import *
router = routers.DefaultRouter()
router.register(r'prescription' , Prescriptionviewset )
urlpatterns = [
    path('drugs/<id>', drugget),
    path('drugdel/<id>', drugdelete),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]
