from django.urls import path
from.import views

urlpatterns = [
    path('qr-reader/', views.read_qr, name = 'qr-reader'),
    path('', views.homepage, name = 'homepage')
]