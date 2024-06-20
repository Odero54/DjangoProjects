# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class NairobiHealthFacilities(models.Model):
    gid = models.AutoField(primary_key=True)
    full_id = models.CharField(max_length=254, blank=True, null=True)
    osm_id = models.CharField(max_length=254, blank=True, null=True)
    osm_type = models.CharField(max_length=254, blank=True, null=True)
    addr_city = models.CharField(max_length=254, blank=True, null=True)
    addr_house = models.CharField(max_length=254, blank=True, null=True)
    addr_stree = models.CharField(max_length=254, blank=True, null=True)
    amenity = models.CharField(max_length=254, blank=True, null=True)
    emergency = models.CharField(max_length=254, blank=True, null=True)
    medical_se = models.CharField(max_length=254, blank=True, null=True)
    name = models.CharField(max_length=254, blank=True, null=True)
    wheelchair = models.CharField(max_length=254, blank=True, null=True)
    contact_ph = models.CharField(max_length=254, blank=True, null=True)
    dispensing = models.CharField(max_length=254, blank=True, null=True)
    health_fac = models.CharField(max_length=254, blank=True, null=True)
    health_f_1 = models.CharField(max_length=254, blank=True, null=True)
    health_f_2 = models.CharField(max_length=254, blank=True, null=True)
    health_f_3 = models.CharField(max_length=254, blank=True, null=True)
    media_vide = models.CharField(max_length=254, blank=True, null=True)
    media_vi_1 = models.CharField(max_length=254, blank=True, null=True)
    medical_1 = models.CharField(db_column='medical__1', max_length=254, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    medical_2 = models.CharField(db_column='medical__2', max_length=254, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    medical_3 = models.CharField(db_column='medical__3', max_length=254, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    medical_4 = models.CharField(db_column='medical__4', max_length=254, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    medical_5 = models.CharField(db_column='medical__5', max_length=254, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    medical_6 = models.CharField(db_column='medical__6', max_length=254, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    medical_7 = models.CharField(db_column='medical__7', max_length=254, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    medical_8 = models.CharField(db_column='medical__8', max_length=254, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    medical_9 = models.CharField(db_column='medical__9', max_length=254, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    medical_10 = models.CharField(max_length=254, blank=True, null=True)
    medical_11 = models.CharField(max_length=254, blank=True, null=True)
    medical_st = models.CharField(max_length=254, blank=True, null=True)
    medical_12 = models.CharField(max_length=254, blank=True, null=True)
    medical_13 = models.CharField(max_length=254, blank=True, null=True)
    opening_ho = models.CharField(max_length=254, blank=True, null=True)
    operationa = models.CharField(max_length=254, blank=True, null=True)
    operatio_1 = models.CharField(max_length=254, blank=True, null=True)
    operator_t = models.CharField(max_length=254, blank=True, null=True)
    contact_em = models.CharField(max_length=254, blank=True, null=True)
    medical_14 = models.CharField(max_length=254, blank=True, null=True)
    medical_15 = models.CharField(max_length=254, blank=True, null=True)
    medical_16 = models.CharField(max_length=254, blank=True, null=True)
    medical_17 = models.CharField(max_length=254, blank=True, null=True)
    medical_18 = models.CharField(max_length=254, blank=True, null=True)
    medical_19 = models.CharField(max_length=254, blank=True, null=True)
    medical_20 = models.CharField(max_length=254, blank=True, null=True)
    medical_21 = models.CharField(max_length=254, blank=True, null=True)
    medical_22 = models.CharField(max_length=254, blank=True, null=True)
    medical_23 = models.CharField(max_length=254, blank=True, null=True)
    medical_24 = models.CharField(max_length=254, blank=True, null=True)
    medical_25 = models.CharField(max_length=254, blank=True, null=True)
    medical_26 = models.CharField(max_length=254, blank=True, null=True)
    medical_27 = models.CharField(max_length=254, blank=True, null=True)
    medical_28 = models.CharField(max_length=254, blank=True, null=True)
    medical_29 = models.CharField(max_length=254, blank=True, null=True)
    medical_30 = models.CharField(max_length=254, blank=True, null=True)
    medical_31 = models.CharField(max_length=254, blank=True, null=True)
    medical_32 = models.CharField(max_length=254, blank=True, null=True)
    medical_33 = models.CharField(max_length=254, blank=True, null=True)
    medical_34 = models.CharField(max_length=254, blank=True, null=True)
    medical_35 = models.CharField(max_length=254, blank=True, null=True)
    health_f_4 = models.CharField(max_length=254, blank=True, null=True)
    health_f_5 = models.CharField(max_length=254, blank=True, null=True)
    medical_36 = models.CharField(max_length=254, blank=True, null=True)
    medical_37 = models.CharField(max_length=254, blank=True, null=True)
    medical_38 = models.CharField(max_length=254, blank=True, null=True)
    medical_39 = models.CharField(max_length=254, blank=True, null=True)
    medical_40 = models.CharField(max_length=254, blank=True, null=True)
    medical_41 = models.CharField(max_length=254, blank=True, null=True)
    medical_42 = models.CharField(max_length=254, blank=True, null=True)
    mapillary = models.CharField(max_length=254, blank=True, null=True)
    survey_dat = models.CharField(max_length=254, blank=True, null=True)
    healthcare = models.CharField(max_length=254, blank=True, null=True)
    source_ref = models.CharField(max_length=254, blank=True, null=True)
    type = models.CharField(max_length=254, blank=True, null=True)
    name_it = models.CharField(max_length=254, blank=True, null=True)
    media_came = models.CharField(max_length=254, blank=True, null=True)
    media_ca_1 = models.CharField(max_length=254, blank=True, null=True)
    operator = models.CharField(max_length=254, blank=True, null=True)
    healthca_1 = models.CharField(max_length=254, blank=True, null=True)
    addr_full = models.CharField(max_length=254, blank=True, null=True)
    electricit = models.CharField(max_length=254, blank=True, null=True)
    health_ame = models.CharField(max_length=254, blank=True, null=True)
    insurance_field = models.CharField(db_column='insurance_', max_length=254, blank=True, null=True)  # Field renamed because it ended with '_'.
    is_in_heal = models.CharField(max_length=254, blank=True, null=True)
    url = models.CharField(max_length=254, blank=True, null=True)
    water_sour = models.CharField(max_length=254, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nairobi_health_facilities'


class NairobiSubCounties(models.Model):
    gid = models.AutoField(primary_key=True)
    constituen = models.CharField(max_length=50, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nairobi_sub_counties'
