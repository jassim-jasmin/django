import datetime

# Create your models here.
from django.db import models
from django.utils import timezone


class Layer(models.Model):
    layer_name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.layer_name

class Layer_Validation(models.Model):
    layer = models.ForeignKey(Layer, on_delete=models.CASCADE)
    locatorData = models.CharField(max_length=500)
    locator_id = models.CharField(max_length=200)
    flag = models.CharField(max_length=5)

    def __str__(self):
        return self.locator_id

class Layer_Connect(models.Model):
    left_layer_name = models.CharField(max_length=200)
    right_layer_name = models.CharField(max_length=200)
    left_connect = models.CharField(max_length=200)
    right_connect = models.CharField(max_length=200)

class Locator(models.Model):
    layer_name = models.CharField(max_length=200)
    locator_id = models.CharField(max_length=200)
    locator_data = models.CharField(max_length=500)
    connect = models.ForeignKey(Layer, on_delete=models.CASCADE)