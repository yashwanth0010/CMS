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