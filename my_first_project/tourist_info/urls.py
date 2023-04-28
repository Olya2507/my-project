from django.urls import path
from . import views

urlpatterns = [
    path('', views.tourist_info),
    path('sale/', views.sale),
    path('payment/', views.payment)
]