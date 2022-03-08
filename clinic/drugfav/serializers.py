from rest_framework import serializers
from .models import FavDrugs

class FavDrugSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavDrugs
        fields = '__all__'