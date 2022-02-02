from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import Livros
# Register your models here.

@admin.register(Livros)
class LivrosAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'editora', 'autor', 'cod_book', 'user')
