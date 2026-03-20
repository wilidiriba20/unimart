from django.urls import path
from products.views import index, sell, product_detail,delete

app_name = 'products'

urlpatterns = [
    path("", index, name='index'),
    path('sell/', sell, name='sell'),  # Add new product
    path('sell/<int:product_id>/', sell, name='edit_sell'),  # Edit existing product
    path('product/<int:id>/', product_detail, name='product_detail'),
    path("delete/<int:product_id>/", delete, name='delete'),  # Delete

]