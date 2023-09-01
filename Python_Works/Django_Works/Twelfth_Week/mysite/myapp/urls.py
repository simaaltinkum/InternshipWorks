from django.urls import path
from.import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('homepage/', views.homepage, name = 'home'),
    # path('register/', views.register, name = 'register'),
    # path('login/', auth_views.LoginView.as_view(), name = 'login')
    path('login/', views.login_user, name = 'login'),
    path('logout/', views.logout_user, name = 'logout'),
    path('tweet/', views.tweet_user, name = 'tweet')
    ]