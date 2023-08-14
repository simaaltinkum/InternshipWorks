from django.shortcuts import render
from meseapp.models import WebSiteAyarlari, Items

def homepage(request):
    collapse_text = WebSiteAyarlari.objects.get(pk=1)
    nav_item = Items.objects.all()

    context = {
        'collapse_text': collapse_text,
        'nav_item': nav_item,
    }
    return render(request, 'homepage.html', context)
