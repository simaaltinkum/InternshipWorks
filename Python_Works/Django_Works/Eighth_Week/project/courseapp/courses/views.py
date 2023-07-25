from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('homepage')

def courses(request):
    return HttpResponse('course list')
