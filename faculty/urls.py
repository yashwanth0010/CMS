from django.contrib import admin
from django.urls import path,include
from django.conf import settings #add this
from django.conf.urls.static import static
from faculty import views
urlpatterns = [
    path('fhome', views.fhome, name='fhome'),
    path('leave_req', views.leave_req, name='leave_req'),
    path('fstd', views.f_std, name='fstd'),

]