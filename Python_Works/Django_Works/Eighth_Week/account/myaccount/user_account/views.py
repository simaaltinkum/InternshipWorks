from django.shortcuts import render
from django.http import HttpResponse

operate = {
    "operations": [
        {
            "paying":"debt paying",
            "loan":"borrowing money"
        }
    ]
}


def index(request):
    operation = operate["operations"]
    return HttpResponse(request)
