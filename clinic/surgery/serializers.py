from rest_framework import serializers
from main.models import Surgery

class SurgerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Surgery
        fields = '__all__'
