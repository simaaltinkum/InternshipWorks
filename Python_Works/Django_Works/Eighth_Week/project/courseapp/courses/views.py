from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse

data = {
    "programming":"Courses which are programming category",
    "web-developing":"Courses which are web-developing category",
    "mobile":"Courses which are mobile category",
}
def courses(request):
    return HttpResponse('Course list')

def details(request, course_name):
    return HttpResponse(f"{course_name} detail page")

def getCoursesByCategory(request, category_name):
    try:
        category_text = data[category_name];
        return HttpResponse(category_text)
    except:
        return HttpResponseNotFound("False category choose")
def getCoursesCategoryId(request, category_id):
    category_list = list(data.keys())
    if(category_id > len(category_list)):
        return HttpResponseNotFound("False category choose")
    category_name = category_list[category_id - 1]

    redirect_url = reverse('courses_by_cetegory', args=[category_name])
    return redirect(redirect_url)