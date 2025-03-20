from django.db import models

# Create your models here.
class Injury(models.Model):
    place = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    symptoms = models.TextField()
    recommendations = models.TextField()
    