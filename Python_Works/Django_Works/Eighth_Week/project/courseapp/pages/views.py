from django.shortcuts import render
from django.http import HttpResponse
def aboutus(request):
    return HttpResponse("About Us")

def communication(request):
    return HttpResponse("Comminicate Us")

def home(request):
    return HttpResponse('Homepage')

