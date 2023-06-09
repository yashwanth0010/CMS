from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import auth
from django.db import connections
import base64
from .models import User,Faculty,Student
from faculty.models import Faculty_data
from std.models import Student_data
from django.conf import settings
from django.core.mail import send_mail



#!/usr/bin/env python 
# coding: utf8
# -*- coding: utf-8 -*-
# Register your models here.
# Create your views here.

def index(request):
    if request.method == 'POST':
        if(request.POST.get('flogin' )):
           return redirect('flogin')
        if(request.POST.get('slogin' )):
            return redirect('slogin')
    return render(request, 'index.html')


def fsignup(request):
    if(request.method == 'POST'):
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        fid = request.POST['fid']
        dept= request.POST['dept']
        is_faculty=1
        is_student=0
        email = request.POST['email']
        if User.objects.filter(email = email).exists():
            messages.error(request, 'Email already exists')
            return redirect('fsignup')
        
        elif User.objects.filter(username = username).exists():
            messages.error(request, 'Username already exists')
            return redirect('fsignup')
        
        elif Faculty.objects.filter(fno = fid).exists():
            messages.error(request, 'Faculty id  already exists')
            return redirect('fsignup')
        
        else:
            #creating a new user in the login_user table 
            user = User.objects.create_user(username=username, email=email, password=password,first_name=firstName,last_name=lastName, is_faculty=is_faculty, is_student=is_student)
            user.save()
            #creating a new row with fid in Faculty table with id as user
            fac= Faculty.objects.create(user=user)
            fac.fno=fid
            fac.department=dept
            fac.save()

            # Creating new entry in the faculty table of Data_db of the faculty that is registered
            # Her we are creating a object for faculty class and saving it in the Data_db database faculty table
            name= firstName+lastName
            fdata = Faculty_data(fno=fid , name=name,department=dept,students={},subjects={})
            fdata.save(using='Data_db')
            return redirect('flogin')

        
    return render(request,'Fsignup.html')



def ssignup(request):
    if(request.method == 'POST'):
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        rollno = request.POST['rollno']
        dept= request.POST['dept']
        is_faculty=0
        is_student=1
        if User.objects.filter(email = email).exists():
            messages.error(request, 'Email already exists')
            return redirect('ssignup')
        
        elif User.objects.filter(username = username).exists():
            messages.error(request, 'Username already exists')
            return redirect('ssignup')
        
        elif Student.objects.filter(rollno = rollno).exists():
            messages.error(request, 'Rollno already exists')
            return redirect('ssignup')
        
        else:
            #creating a new user in the login_user table 
            ouser = User.objects.create_user(username=username, email=email, password=password,first_name=firstName,last_name=lastName,is_faculty=is_faculty, is_student=is_student)
            ouser.save()
            #creating a new row with rollno in Student table with id as user
            std= Student.objects.create(user=ouser)
            std.rollno=rollno
            std.department=dept
            std.save()
            # Creating a new entry of student in Data_db student table
            name=firstName+lastName
            std_data = Student_data(rollno = rollno,name=name,department = dept,subjects = {})
            std_data.save(using='Data_db')
            """subject = 'welcome to College of ???'.encode("UTF-8")
            message = f'Hi {ouser.username}, Welcome To college of ??? We are grateful to have you'.encode("UTF-8")
            email_from = settings.EMAIL_HOST_USER.encode("UTF-8")
            recipient_list = [ouser.email, ]
            send_mail( subject, message, email_from, recipient_list,fail_silently=False )"""
            send_mail(
                'Welcome',
                'Welcome To college of ??? We are grateful to have you',
                'cyashwanthkumar@yahoo.com',
                [ouser.email],
                fail_silently=False,
            )

            return redirect('slogin')

        
    return render(request,'Ssignup.html')



def flogin(request):
    if request.method =='POST':

        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            if user.is_faculty == True:
                auth.login(request, user)
                u= Faculty.objects.get(user_id=user.id)
                request.session['fno'] = u.fno
                return redirect('fhome')
            else:
                messages.info(request,'Invalid login')
                return redirect('flogin')
        else:
            messages.info(request,'Invalid login')
            return redirect('flogin')

    return render(request,'Flogin.html')




def slogin(request):
    if request.method =='POST':

        username = request.POST['username']
        password = request.POST['password']
        #global user
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            if user.is_student == True:
                auth.login(request, user)
                #if user is present then go to student table and get rollno woth help of his id in the table which is a primay key
                u= Student.objects.get(user_id=user.id)
                
                #This rollno is accessed in student.views to get data of that particular student
                #usign request.session to get only that rollno the student is logged in and accessing it anywhere
                request.session['rollno'] = u.rollno
                #slogin.rollno= u.rollno
                return redirect('shome')
            else:
                 messages.info(request,'Invalid login')
                 return redirect('slogin')
        else:
            messages.info(request,'Invalid login')
            return redirect('slogin')

    return render(request,'Slogin.html')
    

def logout(request):
    auth.logout(request)
    return redirect('index')

   