from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import auth
from django.db import connections
import base64
from .models import Faculty_data
import login.views as lv
from std.models import StdLeaves,Student_data

# Create your views here.\
def fhome(request):
    fhome.fno = request.session['fno']
    fhome.data = Faculty_data.objects.using('Data_db').filter(fno=request.session['fno']).values()
    #print(data)
    return render(request, 'fhome.html',{'data' : fhome.data[0]})
					

def leave_req(request):
    if request.method=='POST':
        id = request.POST.get("id")
        if(request.POST.get('grant')):
            grant = request.POST.get('grant')
            lea =  StdLeaves.objects.using("Data_db").get(id=id)
            lea.is_granted = 1
            lea.save()
        elif (request.POST.get('reject')):
            reject = request.POST.get('reject')
            lea =  StdLeaves.objects.using("Data_db").get(id=id)
            lea.is_granted = -1
            lea.save()

    data = reversed(StdLeaves.objects.using("Data_db").filter(faculty_id =request.session['fno']).values())
    #print(data)
    return render(request, 'leavereq.html',{'requests' : data})



def f_std(request):
    if request.method == 'POST':
        rollno= request.POST.get('mentee')
        newstd = Faculty_data.objects.using("Data_db").get(fno =request.session['fno'] )
        stds = newstd.students
        if(stds):
            maxi = max(stds.keys())
            maxi = int(maxi)
            maxi=maxi+1
            stds.update({maxi : rollno})
            #print(stds)
        else:
            stds.update({1 : rollno})
            #print(stds)
        newstd.save()
    data =  Faculty_data.objects.using('Data_db').filter(fno=request.session['fno']).values('students')
    if(data[0]['students']):
            
        nums = data[0]['students'].values()
        #print(nums)
        dis ={}
        for num in nums:
            d= Student_data.objects.using('Data_db').get(rollno = num)
            dis[num] = {
                'rollno' : d.rollno,
                'name' : d.name,
                'dept' : d.department,
                'attd' : d.attendence
            }
        print(dis)

        return render(request, 'fstd.html', {"data" : dis})
    return render(request, 'fstd.html')


