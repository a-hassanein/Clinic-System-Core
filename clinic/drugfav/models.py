from django.db import models

# Create your models here.
class FavDrugs(models.Model):
    drugid = models.AutoField(primary_key=True)
    favname = models.CharField(max_length=100)
    favdose = models.CharField(max_length=100)
    favdosageform = models.CharField(max_length=50)
    favfrequency = models.CharField(max_length=100)
    favnoofdays = models.IntegerField()
    favduration = models.CharField(max_length=50)
    favinstructions = models.TextField()