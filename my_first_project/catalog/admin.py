from django.contrib import admin
from .models import Category, Mytour


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug'] #используется для задания полей, которые могут быть отредактированы на странице отображения списка сайта администрирования. Это позволит редактировать несколько строк одновременно. Любое поле в list_editable также должно быть указано в атрибуте list_display, поскольку могут быть изменены только отображаемые поля.
    prepopulated_fields = {'slug': ('name',)} #атрибут prepopulated_fields, чтобы указать поля, в которых значение автоматически задается с использованием значения других полей


admin.site.register(Category, CategoryAdmin)


class MytourAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'day', 'hotel', 'data_tour', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Mytour, MytourAdmin)
