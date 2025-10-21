from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import User


class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Important Dates"), {
            "fields": ("last_login",),
        }),
        (_("Django Permissions"), {
            "fields": (
                "is_active",
                "is_staff",
                "is_superuser",
                "groups",
                "user_permissions",
            )
        }),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email",  "password1", "password2"),
        }),
    )
    list_display = (
        "email",
        "is_staff",
        "is_active",
    )
    search_fields = (
        "email",
    )
    ordering = ["email"]


admin.site.register(User, UserAdmin)
