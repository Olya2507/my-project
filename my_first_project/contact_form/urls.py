from django.urls import path
from .views import FeedBackView, SuccessView


urlpatterns = [

    path('', FeedBackView.as_view(), name='contact_form'),
    path('success/', SuccessView.as_view(), name='success'),
]