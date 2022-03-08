from rest_framework import serializers
from labfav.models import FavLabs, FavScans

class FavBillSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavLabs
        fields = '__all__'

class FavScanSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavScans
        fields = '__all__'

