from django.urls import path
from .import views

urlpatterns = [
    path('list', views.courses),
    path('<course_name>', views.details),
    path('category/<int:category_id>', views.getCoursesCategoryId),
    path('category/<str:category_name>', views.getCoursesByCategory, name='courses_by_category'),
]