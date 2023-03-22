from django.contrib import admin
from django.urls import path,include
from django.conf import settings #add this
from django.conf.urls.static import static
from login import views
from std import urls
urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('flogin', views.flogin, name='flogin'),
    path('slogin', views.slogin, name='slogin'),
    path('fsignup', views.fsignup, name='fsignup'),
    path('ssignup', views.ssignup, name='ssignup'),
    path('logout', views.logout, name='logout'),
    path('', include('std.urls'))

]