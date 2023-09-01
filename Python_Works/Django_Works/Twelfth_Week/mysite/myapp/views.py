from django.shortcuts import render
from .forms import TweetModelForm
from .models import Tweet
from django.contrib.auth import authenticate, login

def homepage(request):
    tweet_list = Tweet.objects.all()

    context = {
        'tweet_list': tweet_list
    }
    return render(request,'homepage.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request,'loginsuccess.html')
        else:
            return render (request,'invalidlogin.html')

    return render(request, 'login.html')

def tweet_user(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = TweetModelForm(request.POST)
            if form.is_valid():
                form.save()
                return render(request, 'tweetuser.html')
            else:
                form = TweetModelForm()
                return render(request, 'register.fail.html')
        return render(request, 'tweetuser.html')
