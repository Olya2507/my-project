from . import views
from django.urls import path


app_name = 'contact'
urlpatterns = [
    path('', views.contacts, name='contact'),
    path('contact9', views.contact, name='contact9'),

    ]