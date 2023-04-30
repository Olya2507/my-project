from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from catalog.models import Mytour
from .cart import Cart
from .forms import CartAddMytourForm
from django.http import HttpResponse
from coupons.forms import CouponApplyForm

""" Это представление для добавления продуктов в корзину или обновления количества для существующих продуктов. 
Мы используем декоратор require_POST, чтобы разрешить только POST запросы, поскольку это представление изменит данные. 
Представление получает ID продукта в качестве параметра. Мы извлекаем экземпляр продукта с заданным ID и проверяем CartAddProductForm.
 Если форма валидна, мы либо добавляем, либо обновляем продукт в корзине. Представление перенаправляет по URL-адресу cart_detail,
  который будет отображать содержимое корзины. Мы собираемся создать cart_detail представление в ближайшее время."""


@require_POST
def cart_add(request, mytour_id):
    cart = Cart(request)
    mytour = get_object_or_404(Mytour, id=mytour_id)
    form = CartAddMytourForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(mytour=mytour,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')

"""Представление cart_remove получает id продукта в качестве параметра. Мы извлекаем экземпляр продукта с заданным id и удаляем 
продукт из корзины. Затем мы перенаправляем пользователя на URL-адрес cart_detail."""


def cart_remove(request, mytour_id):
    cart = Cart(request)
    mytour = get_object_or_404(Mytour, id=mytour_id)
    cart.remove(mytour)
    return redirect('cart:cart_detail')

"""Представление cart_detail выводит на экран текущее состояние корзины."""

def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddMytourForm(
                            initial={'quantity': item['quantity'],
                            'update': True})
    coupon_apply_form = CouponApplyForm()
    return render(request,
                  'cart/detail.html',
                  {'cart': cart,
                   'coupon_apply_form': coupon_apply_form})
