from django.urls import path
from . import views

app_name = 'messaging'

urlpatterns = [
    path('chat/<int:product_id>/', views.chat_detail, name='chat_detail'),
    path('rate/<int:product_id>/', views.rate_seller, name='rate_seller'),
]