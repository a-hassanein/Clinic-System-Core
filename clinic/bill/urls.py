

from django.urls import path,include
from rest_framework import routers
from .views import *
router = routers.DefaultRouter()
# router.register(r'users', Userlist)
# router.register(r'users/<id>', userUpadateOrDelete)



urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('myapi/<id>', include(router.urls)),
    # path('users/<id>', include(router.urls)),
    path('bill/<id>', BillGet),
    path('billpost', BillPost)

]