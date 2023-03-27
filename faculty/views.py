from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import auth
from django.db import connections
import base64
from .models import Faculty_data
import login.views as lv
from std.models import StdLeaves

# Create your views here.\
def fhome(request):
    fhome.fno = request.session['fno']
    data = Faculty_data.objects.using('Data_db').filter(fno=request.session['fno']).values()
    #print(data)
    return render(request, 'fhome.html',{'data' : data[0]})
					

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
    print(data)
    return render(request, 'leavereq.html',{'requests' : data})



