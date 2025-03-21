from django.db import models

# Create your models here.

class Injury(models.Model):
    place = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    symptoms = models.TextField()
    recommendations = models.TextField(default="Консултирайте се с медицинско лице.")

class Place(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"

class Cause(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"

class Symptom(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, null=True)
    cause = models.ForeignKey(Cause, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"

