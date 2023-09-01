from django.urls import path
from.import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('homepage/', views.homepage, name = 'homepage'),
    # path('register/', views.register, name = 'register'),
    # path('login/', auth_views.LoginView.as_view(), name = 'login')
    path('login/', views.login_user, name = 'login'),
    path('tweet/', views.tweet_user, name = 'tweet')
    ]