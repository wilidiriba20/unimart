from django.contrib import admin
from django.utils.html import format_html
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # Columns to display in the list view
    list_display = ('image_tag', 'title', 'price', 'seller', 'condition', 'created_at')
    
    # Filters in the right sidebar
    list_filter = ('condition', 'category', 'created_at')
    
    # Search fields
    search_fields = ('title', 'description', 'seller__username')
    
    # Make created_at and image_tag read-only
    readonly_fields = ('created_at', 'image_tag')
    
    # Show the image without a link
    def image_tag(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" class="admin-product-img" style="max-width:80px; max-height:80px; border-radius:6px; object-fit:cover;" />',
                obj.image.url
            )
        return "-"
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True  # not needed in modern Django but safe to leave