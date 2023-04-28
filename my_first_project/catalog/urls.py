from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'catalog'

urlpatterns = [
    path('', views.mytour_list, name='mytour_list'),
    path('<slug:category_slug>/', views.mytour_list, name='mytour_list_by_category'),
    path('<int:id>/<slug:slug>/', views.mytour_detail, name='mytour_detail'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#Это шаблоны URL-адресов для каталога продуктов. Мы определили два различных шаблона URL-адреса для представления product_list:
# шаблон с именем product_list, который вызывает product_list view без каких-либо параметров;
# и шаблон с именем product_list_by_category, который предоставляет параметр category_slug в представлении для фильтрации продуктов
# по данной категории.
# Мы добавили шаблон для выносного элемента product_detail, который передает в представление параметры id и slug для
# извлечения конкретного продукта.