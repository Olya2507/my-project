from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Category, Mytour
from cart.forms import CartAddMytourForm



def mytour_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    mytours = Mytour.objects.filter(available=True) #Мы отфильтруем запрос с available=True, чтобы получить только доступные продукты.
    # Мы будем использовать необязательный параметр category_slug, чтобы дополнительно фильтровать продукты по данной категории.
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        mytours = mytours.filter(category=category)
    return render(request,
                  'mytour/mytour_list.html',
                  {'category': category,
                   'categories': categories,
                   'mytours': mytours})


def mytour_detail(request, id, slug):
    mytour = get_object_or_404(Mytour,
                                id=id,
                                slug=slug,
                                available=True)
    cart_mytour_form = CartAddMytourForm()
    return render(request, 'mytour/mytour_detail.html', {'mytour': mytour, 'cart_mytour_form': cart_mytour_form})

#Для получения экземпляра Product в product_detail view рассчитываются параметры id и slug. Этот экземпляр можно получить
# только с помощью id, поскольку он является уникальным атрибутом. Тем не менее, в URL-адрес можно добавить slug для создания
# удобных URL-адресов для продуктов.