from django.urls import path
from.import views

urlpatterns = [
    path('qr-reader/', views.read_qr, name = 'qr-reader'),
    path('qr-list/', views.list, name = 'qr-data'),
    path('type/', views.type, name = 'type'),
    path('', views.homepage, name = 'homepage')
]