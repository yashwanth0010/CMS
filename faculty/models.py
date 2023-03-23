from django.db import models

# Create your models here.


class Faculty_data(models.Model):
    fno = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=25)
    department = models.CharField(max_length=10)
    subjects = models.JSONField()
    students = models.JSONField()

    class Meta:
        managed = True
        db_table = 'faculty'
