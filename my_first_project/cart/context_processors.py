from .cart import Cart

def cart(request):
    return {'cart': Cart(request)}

"""мы создаем объект корзины с помощью объекта request и делаем его доступным для шаблонов в виде переменной с именем cart."""