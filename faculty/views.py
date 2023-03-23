from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import auth
from django.db import connections
import base64
from .models import Faculty_data
import login.views as lv

# Create your views here.\
def fhome(request):
    fno = lv.fno
    data = Faculty_data.objects.using('Data_db').filter(fno=fno).values()
    print(data)
    return render(request, 'fhome.html',{'data' : data[0]})


