from django.db import models

# Create your models here.

class Injury(models.Model):
    place = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    symptoms = models.TextField()
    recommendations = models.TextField(default="Консултирайте се с медицинско лице.")


class Symptom(models.Model):
    place = models.IntegerField(null=True)
    name = models.CharField(max_length=255)
    key = models.CharField(max_length=10)

    def save(self, *args, **kwargs):
        self.key = str(self.place) + self.name[:3]
        super(Symptom, self).save(*args, **kwargs)

class Cause(models.Model):
    name = models.CharField(max_length=255)
    symptoms = models.ForeignKey(Symptom, on_delete=models.CASCADE, null=True)
    #symp = Symptom.key