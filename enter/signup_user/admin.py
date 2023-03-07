from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
# class CustomUserAdmin(UserAdmin):
#     # Add your customizations for the admin page here.
#     ordering = ('email',)

class CustomUserAdmin(admin.ModelAdmin):
    fields = ['email', 'password', 'last_name']

# admin.site.register(CustomUser, CustomUserAdmin)
