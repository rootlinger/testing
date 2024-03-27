from django.db import models
from django.utils import timezone


# Create your models here.
class Human(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    date_birth = models.DateField()
    place_residence = models.CharField(max_length=255)
