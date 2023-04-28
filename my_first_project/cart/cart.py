from decimal import Decimal
from django.conf import settings
from catalog.models import Mytour

#класс Cart, который позволит нам управлять корзиной для покупок. Требуется инициализация корзины с помощью объекта request.
# Мы храним текущую сессию с помощью self.session = request.session, чтобы сделать его доступным для других методов класса Cart.
# Во-первых, мы пытаемся получить корзину с текущей сессии с помощьюse lf.session.get(settings.CART_SESSION_ID).
# Если в сессии отсутствует корзина, то мы создадим сессию с пустой корзиной, установив пустой словарь в сессии.
# Мы ожидаем, что наш словарь корзины будет использовать коды продуктов в качестве ключей и словарь с количеством и ценой
# в качестве значения для каждого ключа. Таким образом, мы можем гарантировать, что продукт не будет добавлен в корзину
# более одного раза; можно также упростить доступ к данным элементов корзины.


class Cart(object):

    def __init__(self, request):
        """
        Инициализируем корзину
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, mytour, quantity=1, update_quantity=False):
        """
        Добавить продукт в корзину или обновить его количество.
        """
        mytour_id = str(mytour.id)
        if mytour_id not in self.cart:
            self.cart[mytour_id] = {'quantity': 0,
                                     'price': str(mytour.price)}
        if update_quantity:
            self.cart[mytour_id]['quantity'] = quantity
        else:
            self.cart[mytour_id]['quantity'] += quantity
        self.save()



    def save(self):
        # Обновление сессии cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # Отметить сеанс как "измененный", чтобы убедиться, что он сохранен
        self.session.modified = True



    def remove(self, mytour):
        """
        Удаление товара из корзины. Метод remove() удаляет заданный продукт из словаря корзины и вызывает метод save()
        для обновления корзины в сессии.
        """
        mytour_id = str(mytour.id)
        if mytour_id in self.cart:
            del self.cart[mytour_id]
            self.save()

    def __iter__(self):
        """
        Перебор элементов в корзине и получение продуктов из базы данных. В методе __iter__() мы извлекаем экземпляры продукта,
         в корзине, чтобы включить их в номенклатуры корзины. Наконец, мы проходим по элементам корзины, преобразуя цену номенклатуры
         обратно в десятичное число и добавляя атрибут total_price к каждому элементу. Теперь можно легко выполнить итерацию по товарам в корзине.
        """
        product_ids = self.cart.keys()
        # получение объектов product и добавление их в корзину
        mytours = Mytour.objects.filter(id__in=product_ids)
        for mytour in mytours:
            self.cart[str(mytour.id)]['mytour'] = mytour

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """
        Подсчет всех товаров в корзине. пользовательский метод __len__(), чтобы вернуть общее количество элементов, хранящихся в корзине.
        """
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        """
        Подсчет стоимости товаров в корзине.
        """
        return sum(Decimal(item['price']) * item['quantity'] for item in
                   self.cart.values())

    def clear(self):
        # удаление корзины из сессии
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True