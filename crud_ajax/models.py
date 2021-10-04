from django.db import models


# Create your models here.
class Welbex(models.Model):
    name = models.CharField(max_length=30, blank=True)
    quantity = models.IntegerField(blank=True)
    distance = models.FloatField(default=0)
    date = models.DateField(blank=True)

    def __str__(self):
        return self.name
