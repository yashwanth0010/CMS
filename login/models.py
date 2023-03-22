from django.db import models
from django.contrib.auth.models import AbstractUser

#creating a custom login with additional fields of is_faculty and is_student
class User(AbstractUser):
    is_faculty = models.BooleanField('Is Faculty',default=False)
    is_student = models.BooleanField('Is student',default=False)

# creating new tables of Student and Faculty with the given fields 
#These are additional tables whose id will be of same as User that is registered
#When a new user gets created with help of views code the data will be filled in these tabels 
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    rollno = models.CharField(max_length=20)
    department = models.CharField(max_length=20)


class Faculty(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    fno = models.CharField(max_length=20)
    department = models.CharField(max_length=20)
