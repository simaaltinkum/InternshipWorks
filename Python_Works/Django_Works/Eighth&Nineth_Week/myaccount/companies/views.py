from django.shortcuts import render

from .forms import CompaniesForm, OperationForm
from .models import Companies, Operation


def create_company(request):
    if request.method == 'POST':
        form = CompaniesForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "index.html")
        else:
            return render(request, 'change.html')
    else:
        form = CompaniesForm()
    return render(request, 'index.html')

def showCompany(request):
    account_list = Companies.objects.all()
    context = {
        "account_list": account_list
    }
    return render(request, "show.html", context)

def selectCompany(request):

    account_list = Companies.objects.all()
    context = {
        "account_list": account_list
    }

    return render(request, "select.html", context)

def money(request):
    if request.method == 'POST':
        form = OperationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "money.html")
    else:
        form = OperationForm()
    return render(request, 'money.html')

def showMoney(request):
    name_list = Companies.objects.all()
    context = {
        "name_list": name_list
    }
    return render(request, "showMoney.html", context)

def sum(request):
     account_list = Operation.objects.all()
     name_list = Companies.objects.all()
     context = {
         "account_list": account_list,
         "name_list": name_list
     }
     return render(request, "summary.html", context)