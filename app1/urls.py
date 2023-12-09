from django.urls import path
from app1.views import *
app_name='muralidhar_155'
urlpatterns=[
    path('msd/',msd,name='msd'),
    path('msd2/',msd2,name='msd2')


]