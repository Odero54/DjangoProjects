from django.db import models
from django.contrib.gis.db import models

# Create your models here.
class NairobiHealthFacilities(models.Model):
    gid = models.AutoField(primary_key=True)
    geom = models.PointField(blank=True, null=True)
    addr_city = models.CharField(db_column='addr_city', max_length=254, blank=True, null=True) # Field renamed to remove unsuitable characters.
    addr_stree = models.CharField(db_column='addr_stree', max_length=254, blank=True, null=True) # Field renamed to remove unsuitable characters.
    name = models.CharField(max_length=254, blank=True, null=True)
    contact_phone = models.CharField(db_column='contact_ph', max_length=254, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nairobi_health_facilities'

class NairobiSubCounties(models.Model):
    gid = models.AutoField(primary_key=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    constituen = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nairobi_sub_counties'