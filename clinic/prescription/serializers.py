from rest_framework import serializers
from main.models import Prescription


class PrescriptionSerializer(serializers.ModelSerializer):

    class meta:
        model = Prescription
        fields = '__all__'