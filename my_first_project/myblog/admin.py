from django.contrib import admin
from .models import Myblog, Comment
# Register your models here.
admin.site.register(Myblog)
admin.site.register(Comment)