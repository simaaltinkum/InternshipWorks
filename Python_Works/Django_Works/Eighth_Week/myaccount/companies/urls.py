from django.urls import path
from .import views

urlpatterns = [
    path('companies/', views.create_company, name = "index"),
    path('customer/', views.create_customer, name = "index"),
    path('show-companies/', views.showCompany, name = "show"),
    path('show-customer/', views.showCompany, name = "show"),
]

