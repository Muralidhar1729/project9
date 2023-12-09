from django.shortcuts import render
from django.http import HttpResponse
def msd(request):
    return HttpResponse('today is thursday')
def msd2(request):
    return HttpResponse('tomorrow is friday')


