from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    active = models.BooleanField()

    def __str__(self):
        return self.code

    """модель для хранения купонов. поля:
    code: Код, который туристы должны ввести для применения купона к покупке тура.
    valid_from: Значение datetime, указывает когда купон становится действительным.
    valid_to: Значение datetime, указывает когда купон становится недействительным.
    discount: Применяемая ставка дисконта (это процент, поэтому она принимает значения от 0 до 100). 
    active: Логическое значение, указывающее, активен ли купон."""