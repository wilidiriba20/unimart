from django.shortcuts import render,redirect, get_object_or_404
from .models import Product
from accounts.models import User as CustomUser
from django.db.models import Q


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


def sell(request):
    if request.method == "POST":
        title = request.POST.get('title')
        price = request.POST.get('price')
        description = request.POST.get('description')
        category = request.POST.get('category')
        condition = request.POST.get('condition')
        image = request.FILES.get('image')

        # Create the product using the logged-in custom user
        Product.objects.create(
            title=title,
            price=price,
            description=description,
            category=category,
            condition=condition,
            image=image,
            seller=request.user
        )

        # Handle Add & Add Another
        if "add_another" in request.POST:
            return redirect('sell')

        # Handle normal Add Product
        return redirect('index')

    return render(request, "products/sell.html") 

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'products/product_detail.html', {'product': product})