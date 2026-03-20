from django.shortcuts import render,redirect, get_object_or_404
from .models import Product
from accounts.models import User as CustomUser
from django.db.models import Q
from django.db.models import Avg, Count
from messaging.models import Review  # import Review model
app_name = 'products'

def index(request):
    # Start with all products
    products = Product.objects.all().order_by('-created_at')

    # Get unique categories
    categories = Product.objects.values_list('category', flat=True).distinct()

    # Filter by category
    category = request.GET.get('category')
    if category:
        products = products.filter(category=category)

    # Filter by condition
    condition = request.GET.get('condition')
    if condition:
        products = products.filter(condition=condition)

    # Filter by price
    max_price = request.GET.get('max_price')
    if max_price:
        products = products.filter(price__lte=max_price)

    # Search
    query = request.GET.get('q')
    if query:
        products = products.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(category__icontains=query)
        )

    # Sorting
    sort = request.GET.get('sort')
    if sort == 'price_low':
        products = products.order_by('price')
    elif sort == 'price_high':
        products = products.order_by('-price')
    else:
        products = products.order_by('-created_at')

    context = {
        'products': products,
        'categories': categories
    }

    return render(request, 'products/index.html', context)


# products/views.py



def sell(request, product_id=None):
    if product_id:
        # Editing existing product
        product = get_object_or_404(Product, id=product_id, seller=request.user)
    else:
        product = None

    if request.method == "POST":
        title = request.POST.get('title')
        price = request.POST.get('price')
        description = request.POST.get('description')
        category = request.POST.get('category')
        condition = request.POST.get('condition')
        image = request.FILES.get('image')
        
        if product:
            # Update existing product
            product.title = title
            product.price = price
            product.description = description
            product.category = category
            product.condition = condition
            if image:  # Only update image if a new one is uploaded
                product.image = image
            product.save()
        else:
            # Add new product
            Product.objects.create(
                title=title,
                price=price,
                description=description,
                category=category,
                condition=condition,
                image=image,
                seller=request.user
            )

        if "add_another" in request.POST:
            return redirect('products:sell')
        return redirect('products:index')

    # GET request → show the form (pre-filled if editing)
    context = {'product': product}
    return render(request, "products/sell.html", context)
def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    seller = product.seller

    # Calculate seller ratings
    seller_stats = Review.objects.filter(seller=seller).aggregate(
        avg_rating=Avg('rating'),
        total_reviews=Count('id')
    )

    context = {
        'product': product,
        'avg_rating': seller_stats['avg_rating'] or 0,
        'total_reviews': seller_stats['total_reviews'] or 0
    }

    return render(request, 'products/product_detail.html', context)

def delete(request, product_id):
    product = get_object_or_404(Product, id=product_id, seller=request.user)
    product.delete()
    return redirect('dashbord:dashboard')  # Go back to dashboard after deleting