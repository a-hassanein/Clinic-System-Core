from rest_framework import serializers
from main.models import Clinic

class ClinicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinic
        fields = '__all__'