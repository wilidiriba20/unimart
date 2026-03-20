from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from accounts.models import User
from products.models import Product
from messaging.models import Message

# -------------------------------
# Custom User Admin
# -------------------------------
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'first_name', 'last_name', 'university', 'is_staff')
    ordering = ('email',)
    
    # Remove 'groups' field from the user form
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'university')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions')}),  # groups removed
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    # Add form (for creating new users)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'university', 'is_staff', 'is_superuser', 'user_permissions'),
        }),
    )

# Register the custom UserAdmin
admin.site.register(User, CustomUserAdmin)

# Optionally unregister Group from admin sidebar
admin.site.unregister(Group)



