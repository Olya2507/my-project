from django.urls import path
from . import views

urlpatterns = [
    path('', views.account, name="account"),
    path("signup/", views.SignUp.as_view(), name="signup"),
    ]

