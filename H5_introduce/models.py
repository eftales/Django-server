from django.db import models

# Create your models here.


class class_H5_introduce(models.Model):
    # 我规定了 class_H5_introduce 只有title context两个属性

    title = models.CharField(max_length=30)
    content = models.TextField()
    J_url = models.TextField()
    J_img = models.TextField()


class class_H5_func(models.Model):
    title = models.CharField(max_length=30)
