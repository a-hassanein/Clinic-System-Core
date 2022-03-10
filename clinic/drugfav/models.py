from django.db import models

# Create your models here.
class FavDrugs(models.Model):
    drugid = models.AutoField(primary_key=True)
    favname = models.CharField(max_length=100)
    favdose = models.CharField(max_length=100)
   