from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Additional Info", {'fields': ('company_ID',)}),
    )
    if admin.site.is_registered(User):
        admin.site.unregister(User)

admin.site.register(User, CustomUserAdmin)







