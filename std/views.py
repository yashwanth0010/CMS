from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import auth
from django.db import connections
import base64
from  .models import Student_data,StdLeaves
import login.views as lv
from faculty.models import Faculty_data


# This is a function which gets data from student table in 2nd database and send to html
def shome(request):
    #global rollno
    shome.rollno =request.session['rollno']
    #rollno=shome.rollno
    print(shome.rollno)
    #the below statement gets the data based on the rollno and returns a queryset
    data = Student_data.objects.using('Data_db').filter(rollno=shome.rollno).values()
    #print(data[0]['name'])
    return render(request,'shome.html', {'std' : data[0]})


def sleave(request):
    data = Faculty_data.objects.values_list('name', flat=True).using('Data_db')
    #print(data)
    if(request.method == 'POST'):
        type = request.POST['type']
        reason = request.POST['reason']
        faculty_name = request.POST['name']
        date = request.POST['date']
        dept = request.POST['dept']
        is_granted=0
        fn=  Faculty_data.objects.using('Data_db').filter(name = faculty_name).values()
        #print(fn[0]['fno'])
        fno =fn[0]['fno']
        leave = StdLeaves(std_rollno = shome.rollno, type_of_leave = type, reason_for_leave = reason,  faculty_name = faculty_name,d_o_l = date,department=dept,is_granted = is_granted, faculty_id =fno)
        leave.save(using='Data_db')
        return render(request,'sleave.html',{'names' : data})
    return render(request,'sleave.html',{'names' : data})

def yourleaves(request):
    data = reversed(StdLeaves.objects.using('Data_db').filter(std_rollno=shome.rollno).values())
    #print(data[0])
    return render(request,'yourleaves.html',{'leaves' : data})


