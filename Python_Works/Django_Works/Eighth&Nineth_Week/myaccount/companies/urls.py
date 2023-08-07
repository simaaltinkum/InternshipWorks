from django.urls import path
from .import views

urlpatterns = [
    path('companies/', views.create_company, name = "index"),
    path('show-companies/', views.showCompany, name = "show"),
    path('select/', views.selectCompany, name = "select"),
    path('select/detail/<int:pk>/', views.selectCompanyDetail, name = "selectCompanyDetail"),
    path('operation/', views.money, name = "money"),
    path('show-money/', views.showMoney, name = "showMoney"),
    path('info/', views.info, name = "info"),


]