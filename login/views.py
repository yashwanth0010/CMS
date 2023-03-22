from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import auth
from django.db import connections
import base64
from .models import User,Faculty,Student
from std.views import shome

# Register your models here.
# Create your views here.

def index(request):
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
        
        else:
            #creating a new user in the login_user table 
            user = User.objects.create_user(username=username, email=email, password=password,first_name=firstName,last_name=lastName, is_faculty=is_faculty, is_student=is_student)
            user.save()
            #creating a new row with fid in Faculty table with id as user
            fac= Faculty.objects.create(user=user)
            fac.fno=fid
            fac.department=dept
            fac.save()
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
        
        else:
            #creating a new user in the login_user table 
            ouser = User.objects.create_user(username=username, email=email, password=password,first_name=firstName,last_name=lastName,is_faculty=is_faculty, is_student=is_student)
            ouser.save()
            #creating a new row with rollno in Student table with id as user
            std= Student.objects.create(user=ouser)
            std.rollno=rollno
            std.department=dept
            std.save()
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
        global user
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            if user.is_student == True:
                auth.login(request, user)
                #if user is present then go to student table and get rollno woth help of his id in the table which is a primay key
                u= Student.objects.get(user_id=user.id)
                global rollno
                #This rollno is accessed in student.views to get data of that particular student
                rollno= u.rollno
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

   