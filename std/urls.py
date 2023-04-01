from django.contrib import admin
from django.urls import path,include
from django.conf import settings #add this
from django.conf.urls.static import static
from std import views
urlpatterns = [
    path('shome', views.shome, name='shome'),
    path('sleave',views.sleave, name='sleave'),
    path('yourleaves' , views.yourleaves, name = 'yourleaves'),
    path('subjects', views.subjects, name='subjects'),

]