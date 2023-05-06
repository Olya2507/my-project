from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('catalog:mytour_list_by_category',
                       args=[self.slug])



class Mytour(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='mytours')  # Это ForeignKey модели Category.
    # Это отношение "многие к одному": тур относится к одной категории, а категория содержит несколько туров
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True) # URL тура
    image = models.ImageField(upload_to='mytour/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2) #поле DecimalField. В нем используется десятичное число Python.
    stock = models.PositiveIntegerField() #поле PositiveIntegerField для хранения количества оставшихся мест
    day = models.IntegerField()
    hotel = models.CharField(max_length=200, db_index=True)
    data_tour = models.DateTimeField(blank=False)
    available = models.BooleanField(default=True) #Это булево значение, указывающее, доступен ли тур. Позволяет включить/отключить тур в каталоге.
    created = models.DateTimeField(auto_now_add=True) #Это поле хранит дату когда был создан объект
    updated = models.DateTimeField(auto_now=True) #В этом поле хранится время последнего обновления объекта.

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
#используем параметр мета index_together, чтобы задать индекс для полей id и slug.
    # Мы определим этот индекс, поскольку мы планируем запросить тур с помощью id и slug.
    # Оба поля индексируются вместе для улучшения представлений для запросов, использующих эти два поля.


    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('catalog:mytour_detail',
                       args=[self.id, self.slug])

#get_absolute_url() — это Конвенция для получения URL-адреса данного объекта. Здесь мы будем использовать шаблоны
# URL-адресов, которые мы только что определили в файле urls.py.