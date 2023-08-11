from django.shortcuts import render

from .forms import CompaniesForm, OperationForm
from .models import Companies, Operation


def add_company(request):
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

def showCompany(request, pk):
    account_list = Companies.objects.get(pk=pk)
    context = {
        "account_list": account_list
    }
    return render(request, "show.html", context)

def info(request):
    account_list = Companies.objects.all()
    context = {
        "account_list": account_list
    }
    render(request, "info.html", context)

def selectCompany(request):

    account_list = Companies.objects.all()
    context = {
        "account_list": account_list
    }

    return render(request, "select.html", context)
def selectCompanyDetail(request, pk):
    operation = Operation.objects.get(pk=pk)
    context = {
        "operation": operation
    }

    return render(request, "detail.html", context)

def money(request, pk):
    if request.method == 'POST':
        form = OperationForm(request.POST)

        if form.is_valid():
            if pk == 1:
                form.save()
            else:
                instance = form.save(commit=False)
                existing_instance = Operation.objects.get(pk=pk)
                existing_instance.delete()
                instance.id = pk
                instance.save()

        return render(request, "money.html")
    else:
        form = OperationForm()
    return render(request, 'money.html', {'form': form})


def showMoney(request):

    name_list = Companies.objects.all()
    context = {
        "name_list": name_list
    }

    return render(request, "showMoney.html", context)

def addOperation(request):

    account_list = Companies.objects.all()
    context = {
        "account_list": account_list
    }

    return render(request, "addop.html", context)

def showInfo(request):

    account_list = Companies.objects.all()
    context = {
        "account_list": account_list
    }

    return render(request, "showinfo.html", context)