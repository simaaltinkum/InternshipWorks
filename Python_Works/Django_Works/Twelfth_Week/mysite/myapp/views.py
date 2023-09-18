from django.shortcuts import render
from .forms import TweetModelForm
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from .models import Tweet
from .serializers import TweetSerializer

def homepage(request):
    tweet_list = Tweet.objects.all()

    context = {
        'tweet_list': tweet_list
    }
    return render(request,'home.html', context)

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

def logout_user(request):
    logout(request)
    return render(request, 'logout.html')

def tweet_user(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = TweetModelForm(request.POST, request.FILES)
            if form.is_valid():
                f = form.save(commit=False)
                f.person = request.user
                f.save()
                return render(request, 'tweetuser.html')
            else:
                print(form.errors)
                form = TweetModelForm()

                return render(request, 'registerfail.html')
        return render(request, 'tweetuser.html')

    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, 'loginsuccess.html')
            else:
                return render(request, 'invalidlogin.html')
        return render(request, 'login.html')

@api_view(['POST'])
def add_tweets(request):
    tweet = TweetSerializer(data=request.data)
    filter_params = {'content__in': request.data}
    if Tweet.objects.filter(**filter_params).exists():
        raise serializers.ValidationError('This data already exists')

    if tweet.is_valid():
        tweet.save()
        print(tweet)
        return Response(tweet.data, status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def view_tweets(request):
    if request.query_params:
        tweet = Tweet.objects.filter(**request.query_params.dict())

    else:
        tweet = Tweet.objects.all()

    if tweet:
        serializer = TweetSerializer(tweet, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
