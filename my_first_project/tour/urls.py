from django.urls import path
from . import views

urlpatterns = [
    path('', views.tour_index, name='tour_index'),
    path('<int:pk>/', views.tour_detail, name='tour_detail'),
    path('tour/', views.tour, name='tour'),
    path('tour_1/', views.tour_1, name='tour_1'),
    path('tour_2/', views.tour_2, name='tour_2'),
    path('tour_3/', views.tour_3, name='tour_3'),
    path('tour_4/', views.tour_4, name='tour_4'),
    path('tour_5/', views.tour_5, name='tour_5'),
]