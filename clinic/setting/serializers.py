from rest_framework import serializers
from main.models import Doctor

class SettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'