from django.urls import path
from products.views import index,sell,product_detail

urlpatterns = [
    path("", index, name='index'),
    path('sell',sell,name='sell'),
    path('product/<int:id>/', product_detail, name='product_detail'),
]
