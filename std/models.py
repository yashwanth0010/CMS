from django.db import models

#This is a table in Data_db which stores data of students in the 2nd database This data is displayed in the home page of the student when logged in
class Student_data(models.Model):
    rollno = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(max_length=30)
    department = models.CharField(max_length=10)
    attendence = models.FloatField()
    subjects = models.JSONField()

    class Meta:
        managed = True
        db_table = 'student'


class StdLeaves(models.Model):
    std_rollno = models.CharField(max_length=20)
    type_of_leave = models.CharField(db_column='type of leave', max_length=20)  # Field renamed to remove unsuitable characters.
    reason_for_leave = models.CharField(db_column='reason for leave', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    is_granted = models.IntegerField()
    faculty_name = models.CharField(max_length=20, blank=True, null=True)
    faculty_id = models.IntegerField(blank=True, null=True)
    d_o_l = models.DateField(db_column='D.O.L', blank=True, null=True)
    department = models.CharField(db_column='Department', max_length=20, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    id = models.AutoField(db_column='ID', primary_key=True)
    class Meta:
        managed = True
        db_table = 'std_leaves'