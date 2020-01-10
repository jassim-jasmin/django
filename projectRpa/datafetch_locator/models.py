import datetime

# Create your models here.
from django.db import models
from django.utils import timezone


class Layer(models.Model):
    layer_name = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.layer_name

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Locator(models.Model):
    layer = models.ForeignKey(Layer, on_delete=models.CASCADE)
    locator_data = models.CharField(max_length=500)
    locator_id = models.CharField(max_length=200)

    def __str__(self):
        return self.locator_data