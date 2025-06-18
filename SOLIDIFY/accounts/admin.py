from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from SOLIDIFY.accounts.forms import AppUserChangeForm, AppUserForm

# Register your models here.
UserModel = get_user_model()

@admin.register(UserModel)
class AppUserAdmin(UserAdmin):
    form = AppUserChangeForm
    add_form = AppUserForm

    list_display = ('username', 'email')

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", 'email', "password1", "password2"),
            },
        ),
    )

    fieldsets = (
        ('Credentials', {'fields': ('username', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', )}),
    )

