from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import auth
from django.db import connections
import base64
from  .models import Student_data
import login.views as lv


# This is a function which gets data from student table in 2nd database and send to html
def shome(request):
    rollno =lv.rollno
    #the below statement gets the data based on the rollno and returns a queryset
    data = Student_data.objects.using('Data_db').filter(rollno=rollno).values()
    #print(data[0]['name'])
    return render(request,'shome.html', {'std' : data[0]})


