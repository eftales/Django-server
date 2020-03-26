from django.db import models

# Create your models here.
class class_probe(models.Model):

    MAC = models.TextField()
    location = models.TextField()
    vector = models.TextField()
    map_num = models.TextField()
    others = models.TextField()

class class_map(models.Model):

    num = models.TextField()
    J_img = models.TextField() #格式是 images/p_XX.jpg