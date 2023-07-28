from datetime import date
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse

data = {
    "programming":"Courses which are in programming category",
    "web-developing":"Courses which are in web-developing category",
    "mobile":"Courses which are in mobile category",
}

db = {
    "courses" : [
        {
            "title": "javascript course",
            "description": "javascript course description",
            "imageUrl": "https://img-c.udemycdn.com/course/750x422/1258436_2dc3_4.jpg",
            "slug": "javascript-course",
            "date": date(2023, 7, 27),
            "is-active": True
        },

        {
            "title": "javascript course",
            "description": "javascript course description",
            "imageUrl": "https://img-c.udemycdn.com/course/750x422/2463492_8344_3.jpg",
            "slug": "javascript-course",
            "date": date(2023, 8, 27),
            "is-active": True
        },

        {
            "title": "javascript course",
            "description": "javascript course description",
            "imageUrl": "https://img-c.udemycdn.com/course/750x422/1662526_fc1c_3.jpg",
            "slug": "javascript-course",
            "date": date(2023, 9, 27),
            "is-active": True
        }
    ],
    "categories": [
        {"id": 1, "name":"programming","slug":"programming"},
        {"id": 2, "name":"web-developing","slug":"web-developing"},
        {"id": 3, "name":"mobile apps","slug":"mobile appds"}
    ]
}

# http://127.0.0.1:8000/courses

def index(request):
    course = db["courses"]
    category_list = list(data.keys())

    return render(request, "courses/index.html",{
        'categories': category_list
    })

def details(request, course_name):
    return HttpResponse(f"{course_name} detail page")

def getCoursesByCategory(request, category_name):
    try:
        category_text = data[category_name];
        return render(request, 'courses/courses.html', {
            'category': category_name,
            'category_text': category_text
        })
    except:
        return HttpResponseNotFound("<h1>False category choose</h2>")

def getCoursesCategoryId(request, category_id):
    category_list = list(data.keys())

    if(category_id > len(category_list)):
        return HttpResponseNotFound("False category choose")

    category_name = category_list[category_id - 1]

    redirect_url = reverse('courses_by_category', args=[category_name])
    return redirect(redirect_url)