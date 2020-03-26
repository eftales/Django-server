from django.db import models

# Create your models here.


class SNSC_data(models.Model):
    BuildingID = models.CharField(max_length=2)
    ClassRoomID = models.CharField(max_length=3)
    NumofStudent = models.CharField(max_length=3)
