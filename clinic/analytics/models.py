from django.db import models

# Create your models here.


class Data(models.Model):
    data_id = models.AutoField(primary_key=True)
    pv = models.IntegerField(null=True)
