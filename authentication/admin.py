from django.contrib import admin
from .models import *

#customizing admin
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_verified','is_active', 'password')



# Register your models here.
admin.site.register(User, UserAdmin)