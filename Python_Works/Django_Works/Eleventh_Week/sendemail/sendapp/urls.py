from django.urls import path
from . import views

urlpatterns = [
    path('', views.send_email, name='send_email'),
    path('gonderilenler/', views.send_gonderilenler, name='send_gonderilenler'),
    path('message/<int:pk>/', views.send_message, name='send_message'),
    path('record/', views.record_email, name='record_email'),
    path('show/', views.show_email, name='show_email'),
]
