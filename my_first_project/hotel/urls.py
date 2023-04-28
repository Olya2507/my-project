from django.urls import path
from . import views

urlpatterns = [
    path('', views.hotel_index, name='hotel_index'),
    path('<int:pk>/', views.hotel_detail, name='hotel_detail'),
]