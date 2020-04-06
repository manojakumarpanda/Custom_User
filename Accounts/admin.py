from django.contrib import admin
from .models import User

# Register your models here.
class User_Admin(admin.ModelAdmin):
    list_display = ['id','email']


admin.site.register(User,User_Admin)