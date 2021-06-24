from django.db import models

# Create your models here.
class DoctorsMini(models.Model):
    id = models.TextField(primary_key=True)
    department = models.TextField(db_column='Department')  # Field name made lowercase.
    specializedField = models.TextField(db_column='SpecializedField')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'doctors_mini'


class CatholicDoc(models.Model):
    id = models.TextField(db_column='Id',primary_key=True)  # Field name made lowercase.
    department = models.TextField(db_column='Department')  # Field name made lowercase.
    specializedfield = models.TextField(db_column='SpecializedField') 
 # Field name made lowercase.
    career = models.TextField(db_column='Career')  # Field name made lowercase.
    education = models.TextField(db_column='Education')  # Field name made lowercase.
    numofthesis = models.TextField(db_column='NumofThesis')  # Field name made lowercase.
    nameofthesis = models.TextField(db_column='NameofThesis')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'catholic_doc'


class SeoulDoc(models.Model):
    id = models.TextField(db_column='Id',primary_key=True)  # Field name made lowercase.
    department = models.TextField(db_column='Department')  # Field name made lowercase.
    specializedfield = models.TextField(db_column='SpecializedField') 
 # Field name made lowercase.
    career = models.TextField(db_column='Career')  # Field name made lowercase.
    education = models.TextField(db_column='Education')  # Field name made lowercase.
    numofthesis = models.TextField(db_column='NumofThesis')  # Field name made lowercase.
    nameofthesis = models.TextField(db_column='NameofThesis')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'seoul_doc'


class SkkuDoc(models.Model):
    id = models.CharField(db_column='Id', max_length=45, primary_key=True)  # Field name made lowercase.
    department = models.CharField(db_column='Department', max_length=45)  # Field name made lowercase.
    specializedfield = models.CharField(db_column='SpecializedField', max_length=255)  # Field name made lowercase.
    career = models.TextField(db_column='Career')  # Field name made lowercase.
    education = models.TextField(db_column='Education')  # Field name made lowercase.
    numofthesis = models.CharField(db_column='NumofThesis', max_length=15)  # Field name made lowercase.
    nameofthesis = models.TextField(db_column='NameofThesis')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'skku_doc'