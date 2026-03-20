from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from products.models import Product
from messaging.models import Message

@login_required
def dashbord(request):
    # ✅ Only latest products
    products = Product.objects.filter(
        seller=request.user
    ).annotate(
        avg_rating=Avg('seller__reviews_received__rating')
    ).order_by('-created_at')

    # ✅ Add message info
    for product in products:
        product.new_messages_count = Message.objects.filter(
            product=product
        ).exclude(sender=request.user).count()

        product.last_message = Message.objects.filter(
            product=product
        ).order_by('-timestamp').first()

    return render(request, 'dashbord/dashboard.html', {
        'products': products
    })