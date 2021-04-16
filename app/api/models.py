from django.db import models

class Resort(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, )
    description = models.TextField()
    country = models.ForeignKey('Country', on_delete=models.DO_NOTHING)
    class Meta:
        ordering = ['-id']

class Country(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=7)
    iso_code = models.CharField(max_length=2)

class Tour(models.Model):
    id = models.AutoField(primary_key=True)
    resort = models.ForeignKey('Resort', on_delete=models.DO_NOTHING)
    takeoff_time = models.DateTimeField()
    end_time = models.DateTimeField()