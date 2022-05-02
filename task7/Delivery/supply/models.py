# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models




class SupplyUser(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(db_column='First_name', max_length=255)  # Field name made lowercase.
    last_name = models.CharField(db_column='Last_name', max_length=255)  # Field name made lowercase.
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    rpassword = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'supply_user'
