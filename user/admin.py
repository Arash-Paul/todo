from django.contrib import admin
from .models import UserModel


# Register your models here.
class UserList(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'password', 'last_login']


admin.site.register(UserModel, UserList)
