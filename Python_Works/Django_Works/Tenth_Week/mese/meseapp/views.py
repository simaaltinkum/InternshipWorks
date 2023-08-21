from django.shortcuts import render
from meseapp.models import WebSiteAyarlari, Items, Title, Email, Telephone, Services, Adresses

def homepage(request):
    collapse_text = WebSiteAyarlari.objects.get(pk=1)
    nav_item = Items.objects.all()
    title = Title.objects.all()
    email = Email.objects.all()
    telephone = Telephone.objects.all()
    services = Services.objects.all()
    adresses = Adresses.objects.all()

    context = {
        'collapse_text': collapse_text,
        'nav_item': nav_item,
        'title': title,
        'email': email,
        'telephone': telephone,
        'services': services,
        'adresses': adresses
    }
    return render(request, 'homepage.html', context)

def index(request):
    collapse_text = WebSiteAyarlari.objects.get(pk=1)
    nav_item = Items.objects.all()
    context = {
        'collapse_text': collapse_text,
        'nav_item': nav_item
    }
    return render(request, 'index.html', context)
