from rest_framework import serializers
from analytics.models import Data

class AnalyticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ("pv")
