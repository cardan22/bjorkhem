from django.shortcuts import render, get_object_or_404
from .models import Product


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


def favorite_products(request):
    """ A view to show favorite products """

    favorite_products = request.user.favorite_products.all()

    context = {
        'products': favorite_products,
    }

    return render(request, 'products/favorite_products.html', context)   
