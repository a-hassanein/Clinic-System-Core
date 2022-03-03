from rest_framework import serializers 
from main.models import Labs

class LabsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Labs
        fields = '__all__'
