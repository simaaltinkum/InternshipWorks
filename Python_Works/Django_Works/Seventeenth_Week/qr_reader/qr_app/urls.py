from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('read/', views.read, name = 'read'),
    path('save/<str:pk>/', views.save, name = 'save'),
    path('search/', views.search, name = 'search'),
    path('list/', views.list, name = 'list'),
    path('', views.homepage, name = 'homepage')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)