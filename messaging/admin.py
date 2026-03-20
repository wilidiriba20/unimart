from django.contrib import admin
from .models import Message, Review


class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'product', 'timestamp', 'is_read')
    list_filter = ('is_read', 'timestamp')
    search_fields = ('sender__username', 'receiver__username', 'content')
    readonly_fields = ('timestamp',)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('reviewer', 'seller', 'product', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('reviewer__username', 'seller__username')
    readonly_fields = ('created_at',)


admin.site.register(Message, MessageAdmin)
admin.site.register(Review, ReviewAdmin)