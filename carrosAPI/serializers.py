from carrosAPI.models import CarsCar, CarsBrand
from rest_framework import serializers

class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarsCar
        fields= '__all__'

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarsBrand
        fields = '__all__'