from django import forms


class CouponApplyForm(forms.Form):
    code = forms.CharField()

    """Это форма, которая будет использоваться пользователем для ввода кода купона."""