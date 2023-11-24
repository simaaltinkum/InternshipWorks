from django.shortcuts import render
from .forms import MyForm

def home(request):
    form = MyForm(request.POST or None)
    context = {'form': form}
    return render(request, 'home.html', context)

