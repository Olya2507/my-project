from django.urls import path
from .import views

urlpatterns = [
    path('', views.place, name='place')
]