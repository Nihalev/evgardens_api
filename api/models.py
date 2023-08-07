from django.db import models

# Create your models here.
class Plants(models.Model):
    product_name = models.CharField(max_length=200)
    product_image = models.CharField(max_length=200000000000000000000000)