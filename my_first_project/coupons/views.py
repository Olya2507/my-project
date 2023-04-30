from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.utils import timezone
from .models import Coupon
from .forms import CouponApplyForm


@require_POST
def coupon_apply(request):
    now = timezone.now()
    form = CouponApplyForm(request.POST)
    if form.is_valid():
        code = form.cleaned_data['code']
        try:
            coupon = Coupon.objects.get(code__iexact=code,
                                        valid_from__lte=now,
                                        valid_to__gte=now,
                                        active=True)
            request.session['coupon_id'] = coupon.id
        except Coupon.DoesNotExists:
            request.session['coupon_id'] = None
    return redirect('cart:cart_detail')

"""Представление coupon_apply проверяет купон и сохраняет его в сессии пользователя. Мы применяем декоратор require_POST 
к этому представлению, чтобы ограничить его учетом запросов. В представлении мы выполняем следующие задачи:

Мы создаем экземпляр формы CouponApplyForm, используя учтенные данные, и проверяем, что форма является валидной.
Если форма является валидной, мы получим код, введенный пользователем из формы cleaned_data. Мы пытаемся извлечь 
объект Coupon с данным кодом. Мы используем поиск в поле iexact, чтобы проверить точное совпадение без учета регистра.
 Купон должен быть активен в данный момент (active=True) и действителен для текущего datetime. Мы используем функцию 
 Джанго timezone.now(), чтобы получить текущую дату и время, сопоставленные с часовым поясом, и сравнить ее с полями 
 valid_from и valid_to, выполняющими lte(меньше или равными) и gte(больше или равным).
Идентификатор купона хранится в сессии пользователя.
Мы перенаправим пользователя на URL-адрес cart_detail, чтобы отобразить корзину с примененным купоном."""