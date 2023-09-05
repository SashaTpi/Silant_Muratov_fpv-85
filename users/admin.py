from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', "first_name", "role", 'is_staff', 'is_superuser', 'date_joined', ]
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),

        (_("Permissions"),{"fields": ("is_active", "is_staff", "is_superuser", "groups", 
                                      "user_permissions", "role",),},),
                                      
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )


admin.site.register(CustomUser, CustomUserAdmin)