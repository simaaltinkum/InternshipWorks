from django.shortcuts import render
from .forms import UsersForm
from .models import Users
def homepage(request):
    return render(request,'homepage.html')

def register(request):
    if request.method == 'POST':
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "registersuccess.html")
        else:
            return render(request, 'registerfail.html')
    else:
        form = UsersForm()
    return render(request, 'register.html')
