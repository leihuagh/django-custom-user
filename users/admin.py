from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreateForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreateForm
    model = CustomUser
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "password",
                    "username",
                    "life_motto"

                )
            },
        ),
        (
            "Personal Info",
            {
                "fields": (
                    "first_name",
                    "last_name",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "password1",
                    "password2",
                ),
            },
        ),
    )

    list_display = ["username", "email", "first_name"]
    search_fields = ["username"]


admin.site.register(CustomUser, CustomUserAdmin)
