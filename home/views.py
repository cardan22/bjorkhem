from django.shortcuts import render
from products.models import Product


def index(request):
    """ A view to return the index page with latest news """

    news_products = Product.objects.filter(category__name='News')[:4]

    context = {
        'news_products': news_products,
    }

    return render(request, 'home/index.html', context)


def contact(request):
    """ A view to return the contact page """
    
    return render(request, 'home/contact.html')


def policy(request):
    """ A view to return the Policy page """
    
    return render(request, 'home/policy.html')
    

