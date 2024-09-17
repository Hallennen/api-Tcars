from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from carrosAPI.models import CarsCar, CarsBrand
from carrosAPI.serializers import CarsSerializer, BrandSerializer

# Create your views here.


class CarsListView(ListAPIView):
    queryset = CarsCar.objects.all()
    serializer_class = CarsSerializer


class CarDetailsView(RetrieveAPIView):
    queryset = CarsCar.objects.all()
    serializer_class = CarsSerializer


#    --------------------- BRAND ----------------------- #
class BrandListView(ListAPIView):
    queryset = CarsBrand.objects.all()
    serializer_class = BrandSerializer