"""
URL configuration for my_first_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('about/', views.about),
    path("place/", include('place.urls')),
    path("hotel/", include('hotel.urls')),
    path("tourist_info/", include('tourist_info.urls')),
    path("calendar_tour/", include('calendar_tour.urls')),
    path("country/", include('country.urls')),
    path("myblog/", include('myblog.urls')),
    path("app/", include('app.urls')),
    path("application8/", include('application8.urls')),
    path("contact/", include('contact.urls')),
    path("project/", include('project.urls')),
    path("tour/", include('tour.urls')),
    path('articles/', include('articles.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('account/', include('account.urls')),
    path('contact_form/', include('contact_form.urls')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('coupons/', include('coupons.urls', namespace='coupons')),
    path('catalog/', include('catalog.urls', namespace='catalog')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)