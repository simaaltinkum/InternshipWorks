from django.shortcuts import render
from django.http import HttpResponse

def courses(request):
    return HttpResponse('Course list')

def details(request):
    return HttpResponse('Course detail page')

def programming(request):
    return HttpResponse('Programming course list')

def mobileapps(request):
    return HttpResponse('Mobile apps course list')

def getCoursesByCategory(request, category):
    text = ""

    if (category == "programming"):
        text = "Courses which are programming category"

    elif (category == "web-developing"):
        text = "Courses which are web-developing"

    else:
        text = "Invalid category choice"

    return HttpResponse(f"{category} Course list")