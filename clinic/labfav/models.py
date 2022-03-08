from django.db import models

# Create your models here.


class FavLabs(models.Model):
    Lab_id = models.AutoField(primary_key=True)
    Lab_name = models.CharField(max_length=100, null=False)


class FavScans(models.Model):
    Scan_id = models.AutoField(primary_key=True)
    Scan_name = models.CharField(max_length=100, null=False)
