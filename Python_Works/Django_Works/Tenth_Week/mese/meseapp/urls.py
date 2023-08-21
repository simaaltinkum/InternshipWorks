from django.urls import path
from.import views
from django.contrib.flatpages import views as flatpages_views

urlpatterns = [
    path('homepage/', views.homepage, name = 'homepage'),
    path('homepage/index.html', views.homepage, name = 'default'),
    path('homepage/about.html', views.homepage, name = 'default'),
    path('homepage/courses.html', views.homepage, name = 'default'),
    path('homepage/teacher.html', views.homepage, name = 'default'),
    path('homepage/blog.html', views.homepage, name = 'default'),
    path('homepage/contact.html', views.homepage, name = 'default'),
]

