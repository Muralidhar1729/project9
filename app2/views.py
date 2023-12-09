from django.shortcuts import render

from django.http import HttpResponse
def msd3(request):
    return HttpResponse('today is thursday(nov)')
def msd4(request):
    return HttpResponse('tomorrow is friday(nov)')

