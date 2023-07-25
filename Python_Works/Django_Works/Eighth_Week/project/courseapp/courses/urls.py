from django.urls import path
from .import views

# http://127.0.0.1:8000/client        => homepage
# http://127.0.0.1:8000/client/home    => homepage
# http://127.0.0.1:8000/client/courses => course list


urlpatterns = [
    path('', views.home ),
    path('homepage/',views.home),
    path('courses/', views.courses),
]