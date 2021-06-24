from django.db import models

# Create your models here.
class DoctorsMini(models.Model):
    id = models.TextField(primary_key=True)
    department = models.TextField(db_column='Department')  # Field name made lowercase.
    specializedField = models.TextField(db_column='SpecializedField')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'doctors_mini'