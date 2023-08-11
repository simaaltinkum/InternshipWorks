from django.urls import path
from .import views

urlpatterns = [
    path('add-companies/', views.add_company, name = "index"),
    path('show-companies/<int:pk>/', views.showCompany, name = "show"),
    path('select/', views.selectCompany, name = "select"),
    path('select/detail/<int:pk>/', views.selectCompanyDetail, name = "selectCompanyDetail"),
    path('operation/<int:pk>/', views.money, name = "money"),
    path('add-operation/', views.addOperation, name = "addop"),
    path('show-money/', views.showMoney, name = "showMoney"),
    path('show-info/', views.showInfo, name = "showInfo"),
    path('show-info/info/<int:pk>/', views.info, name = "info"),
]