from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse

data = {
    "programming":"Courses which are in programming category",
    "web-developing":"Courses which are in web-developing category",
    "mobile":"Courses which are in mobile category",
}

# http://127.0.0.1:8000/courses

def index(request):
    return render(request, "courses/index.html")

def courses(request):
    list_items = ""
    category_list = list(data.keys())

    for category in category_list:
        redirect_url = reverse('courses_by_category', args=[category])
        list_items += f"<li><a href='{redirect_url}'>{category}</a></li>"

    html = f"<h1>Course List</h1><br><ul>{list_items}</ul>"

    return HttpResponse(html)

def details(request, course_name):
    return HttpResponse(f"{course_name} detail page")

def getCoursesByCategory(request, category_name):
    try:
        category_text = data[category_name];
        return HttpResponse(category_text)
    except:
        return HttpResponseNotFound("<h1>False category choose</h2>")

def getCoursesCategoryId(request, category_id):
    category_list = list(data.keys())

    if(category_id > len(category_list)):
        return HttpResponseNotFound("False category choose")

    category_name = category_list[category_id - 1]

    redirect_url = reverse('courses_by_category', args=[category_name])
    return redirect(redirect_url)