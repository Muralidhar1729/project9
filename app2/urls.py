from django.urls import path
from app2.views import *
app_name='murali'
urlpatterns=[
    path('msd3/',msd3,name='msd3'),
    path('msd4/',msd4,name='msd4')
    
]