from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('get_subcategories/', views.get_subcategories, name='get_subcategories'),
    path('save_choices/', views.save_choices, name='save_choices'),
]
