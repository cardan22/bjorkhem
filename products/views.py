from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views import View
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.db.models.functions import Lower
from django.db.models import Q
from .models import Product, Category


def all_products(request):
    """ A view to show all products, including sorting and search queries """
    
    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

        if 'direction' in request.GET:
            direction = request.GET['direction']
            if direction == 'desc':
                sortkey = f'-{sortkey}'
        products = products.order_by(sortkey)    

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect('products')

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


class product_detail(View):
    """ A view to show individual product details """

    template_name = 'products/product_detail.html'

    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)

        favorite = product.favorites.filter(id=request.user.id).exists()

        context = {
            'product': product,
            'favorite': favorite,
        }

        return render(request, self.template_name, context)


class add_favorite_product(LoginRequiredMixin, View):
    """
    View for adding/removing products from user's favorites.
    Allows authenticated users to add or remove products from their favorites.
    If already a favorite, it's removed; otherwise, it's added.
    """

    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)

        is_favorite = product.favorites.filter(id=request.user.id).exists()

        if is_favorite:
            product.favorites.remove(request.user)
            msg = "This product was removed from your favorites."
            messages.warning(request, msg)
        else:
            product.favorites.add(request.user)
            msg = "This product was added to your favorites."
            messages.success(request, msg)

        return redirect(request.META.get('HTTP_REFERER'))


class favorite_products(LoginRequiredMixin, ListView):
    """ A view to show favorite products """
    
    model = Product
    template_name = 'products/favorite_products.html'
    context_object_name = 'favorite_products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            user = self.request.user
            favorite_products = user.favorite_products.all()
            context['favorite_products'] = favorite_products
        return context
   
