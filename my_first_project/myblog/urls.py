from django.urls import path
from . import views


urlpatterns = [
    path('', views.myblog_index, name='myblog_index'),
    path('<int:pk>/', views.myblog_detail, name='myblog_detail'),

]