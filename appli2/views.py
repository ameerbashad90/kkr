from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def pbks(request):
    return HttpResponse('punjab kings')