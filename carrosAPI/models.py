
from django.db import models


class CarsCor(models.Model):
    cor_name = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cars_cor'


class CarsTracao(models.Model):
    tracao_tipo = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cars_tracao'



class CarsBrand(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'cars_brand'



class CarsCar(models.Model):
    model = models.CharField(max_length=200)
    brand = models.ForeignKey(CarsBrand, models.DO_NOTHING)
    factory_year = models.IntegerField(blank=True, null=True)
    model_year = models.IntegerField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    photo = models.CharField(max_length=100, blank=True, null=True)
    plate = models.CharField(max_length=10, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    cor = models.ForeignKey(CarsCor, models.DO_NOTHING, blank=True, null=True)
    tracao = models.ForeignKey(CarsTracao, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cars_car'


