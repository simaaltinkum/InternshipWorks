from django.urls import path
from .import views

urlpatterns = [
    path('', views.home ),
    path('homepage',views.home),
    path('communication',views.communication),
    path('aboutus',views.aboutus),
]