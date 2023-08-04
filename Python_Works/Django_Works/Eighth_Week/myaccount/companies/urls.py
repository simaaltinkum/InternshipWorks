from django.urls import path
from .import views

urlpatterns = [
    path('companies/', views.create_company, name = "index"),
    path('show-companies/', views.showCompany, name = "show"),
    path('select/', views.selectCompany, name = "select"),
    path('operation/', views.money, name = "money"),
    path('show-money/', views.showMoney, name = "showMoney"),
    path('sum/', views.sum, name = "summary"),
]