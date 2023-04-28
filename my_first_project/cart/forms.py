from django import forms

MYTOUR_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddMytourForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=MYTOUR_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

""" Эта форма будет использоваться для добавления продуктов в корзину. Класс CartAddProductForm содержит следующие поля:

quantity : позволяет пользователю выбрать количество между 1-20. Мы используем поле TypedChoiceField с coerce=int для 
преобразования ввода в целое число.

update : позволяет указать, следует ли добавлять сумму к любому существующему значению в корзине для данного продукта (False)
 или если существующее значение должно быть обновлено с заданным значением (True). Для этого поля используется графический 
 элемент HiddenInput, поскольку не требуется показывать его пользователю."""