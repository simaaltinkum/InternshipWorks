from django.urls import path
from.import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('qr-reader/', views.read_qr, name = 'qr-reader'),
    path('qr-list/', views.list, name = 'qr-data'),
    path('type/', views.type, name = 'type'),
    path('', views.homepage, name = 'homepage')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)