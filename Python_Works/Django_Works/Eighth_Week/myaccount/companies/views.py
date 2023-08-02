from django.shortcuts import render, redirect

from .forms import CompaniesForm, CustomerForm
from .models import Companies, Customer


def create_company(request):
    if request.method == 'POST':
        form = CompaniesForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "index.html")
    else:
        form = CompaniesForm()
    return render(request, 'index.html')

def create_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "index.html")
    else:
        form = CustomerForm()
    return render(request, 'index.html')

def showCompany(request):
    account_list = Companies.objects.all()
    context = {
        "account_list": account_list
    }
    return render(request, "show.html", context)

def showCustomer(request):
    account_list = Customer.objects.all()
    context = {
        "account_list": account_list
    }
    return render(request, "show.html", context)