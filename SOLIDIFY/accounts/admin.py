
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from SOLIDIFY.accounts.forms import AppUserChangeForm, AppUserCreationForm
from SOLIDIFY.accounts.models import Profile

# Register your models here.
UserModel = get_user_model()

@admin.register(UserModel)
class AppUserAdmin(UserAdmin):
    form = AppUserChangeForm
    add_form = AppUserCreationForm

    list_display = ('username', 'email')
    search_fields = ('email', )
    ordering = ('pk',)

    # what fields will be shown when we create new user
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


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'user__is_staff')
    list_filter = ('user__is_staff', )