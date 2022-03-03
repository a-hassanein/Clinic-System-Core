from rest_framework import serializers
from main.models import Material

class MaterialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'
