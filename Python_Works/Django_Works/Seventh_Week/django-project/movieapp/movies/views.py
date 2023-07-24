from django.shortcuts import render

categories_list = ["adventure", "romance","dram"]
films_list = [
    {
        "film_name":"film1",
        "explanation":"film1 explanation",
        "picture":"1.jpeg",
        "homepage":True
    },
    {
        "film_name": "film2",
        "explanation": "film2 explanation",
        "picture": "2.jpeg",
        "homepage":True
    },
    {
        "film_name": "film3",
        "explanation": "film3 explanation",
        "picture": "3.jpeg",
        "homepage":False
    },
    {
        "film_name": "film4",
        "explanation": "film4 explanation",
        "picture": "4.jpeg",
        "homepage":False
    }
]
def home(request):
    data = {
        "categories":categories_list,
        "films":films_list
    }
    return render(request, "index.html", data)

def movies(request):
    data = {
        "categories": categories_list,
        "films": films_list
    }
    return render(request, "movies.html",data)