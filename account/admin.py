from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'phone', 'first_name', 'last_name', 'is_staff', 'is_active', 'is_superuser')
    list_filter = ('phone', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('phone', 'email', 'first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('phone',)
    ordering = ('phone',)


admin.site.register(CustomUser, CustomUserAdmin)
