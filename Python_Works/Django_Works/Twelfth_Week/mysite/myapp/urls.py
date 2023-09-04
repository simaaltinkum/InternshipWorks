from django.urls import path
from.import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('homepage/', views.homepage, name = 'home'),
    # path('register/', views.register, name = 'register'),
    # path('login/', auth_views.LoginView.as_view(), name = 'login')
    path('login/', views.login_user, name = 'login'),
    path('logout/', views.logout_user, name = 'logout'),
    path('tweet/', views.tweet_user, name = 'tweet'),
    path('add-tweets/', views.add_tweets, name='add-tweets'),
    path('view-tweets/', views.view_tweets, name='view-tweets'),
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)