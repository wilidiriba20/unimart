from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Avg
from .models import Message, Review
from products.models import Product
from django.contrib.auth import get_user_model

User = get_user_model()

@login_required
def chat_detail(request, product_id):
    """
    Buyer or seller chat page.
    - Buyers chat with seller.
    - Sellers can chat with multiple buyers (buyer_id via GET).
    """
    product = get_object_or_404(Product, id=product_id)
    seller = product.seller
    user = request.user

    buyer_id = request.GET.get('buyer_id')
    selected_buyer = None
    messages = None

    if user == seller:
        # Seller view
        buyers = User.objects.filter(
            sent_messages__receiver=seller,
            sent_messages__product=product
        ).distinct()

        if buyer_id:
            selected_buyer = get_object_or_404(User, id=buyer_id)
            messages = Message.objects.filter(
                product=product
            ).filter(
                Q(sender=seller, receiver=selected_buyer) | Q(sender=selected_buyer, receiver=seller)
            )
            # Mark buyer's messages as read
            Message.objects.filter(sender=selected_buyer, receiver=seller, product=product).update(is_read=True)

    else:
        # Buyer view
        selected_buyer = seller
        messages = Message.objects.filter(
            product=product
        ).filter(
            Q(sender=user, receiver=seller) | Q(sender=seller, receiver=user)
        )
        # Mark seller's messages as read
        Message.objects.filter(sender=seller, receiver=user, product=product).update(is_read=True)

    # Handle sending new message
    if request.method == "POST":
        content = request.POST.get('message_text')
        if content:
            Message.objects.create(
                sender=user,
                receiver=selected_buyer,
                product=product,
                content=content
            )
        # Redirect back to the same page
        if user == seller and selected_buyer:
            return redirect(f"{request.path}?buyer_id={selected_buyer.id}")
        return redirect('messaging:chat_detail', product_id=product.id)

    # Seller rating info
    avg_rating = Review.objects.filter(seller=seller).aggregate(avg=Avg('rating'))['avg'] or 0
    total_reviews = Review.objects.filter(seller=seller).count()

    context = {
        'product': product,
        'seller': seller,
        'buyers': buyers if user == seller else None,
        'selected_buyer': selected_buyer,
        'messages': messages,
        'avg_rating': avg_rating,
        'total_reviews': total_reviews
    }

    return render(request, 'messaging/message.html', context)


@login_required
def rate_seller(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    seller = product.seller

    if request.user == seller:
        return redirect('messaging:chat_detail', product_id=product.id)

    if request.method == 'POST':
        rating = request.POST.get('rating')
        if rating:
            Review.objects.update_or_create(
                reviewer=request.user,
                product=product,
                defaults={
                    'seller': seller,
                    'rating': int(rating)
                }
            )

    return redirect('messaging:chat_detail', product_id=product.id)