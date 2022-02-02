from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import Users
# Register your models here.

@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    list_display = ('nome', 'senha', 'cod_user')
