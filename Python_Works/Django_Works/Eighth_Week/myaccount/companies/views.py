from django.shortcuts import render, redirect

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
            return render(request, "index.html")
    else:
        form = OperationForm()
    return render(request, 'money.html')

def showMoney(request):
    account_list = Operation.objects.all()
    context = {
        "account_list": account_list
    }
    return render(request, "showMoney.html", context)

"""def showCustomer(request):
    account_list = Customer.objects.all()
    context = {
        "account_list": account_list
    }
    return render(request, "show.html", context)"""
"""def create_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "index.html")
    else:
        form = CustomerForm()
    return render(request, 'index.html')"""

"""def delete():
    Customer.objects.all().delete()
    Companies.objects.all().delete()
    context = {
        "account_list": account_list
    }
    return render(request,"delete.html", context)"""