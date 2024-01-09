from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views import View
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models.functions import Lower
from django.db.models import Q
from .models import Product, Category, RelatedProduct
from .forms import ProductForm


def all_products(request):
    """A view to show all products, including sorting and search queries"""

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
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)
        else:
            # Default sorting by added_date if no sorting option is selected
            products = products.order_by('-posted_date')

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!"
                )
                return redirect(reverse('products'))

            queries = (
                Q(name__icontains=query) | Q(description__icontains=query)
            )
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
    """A view to show individual product details"""

    template_name = 'products/product_detail.html'

    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        related_products = (
            RelatedProduct.objects.filter(from_product=product)
            .select_related('to_product')[:4]
        )
        favorite = product.favorites.filter(id=request.user.id).exists()

        context = {
            'product': product,
            'favorite': favorite,
            'related_products': related_products,
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
    """A view to show favorite products"""

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


@login_required
def add_product(request):
    """Add a product to the store"""

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.save()

            # Save related products
            related_products = form.cleaned_data.get('related_products')
            if related_products:
                for related_product in related_products:
                    RelatedProduct.objects.create(
                        from_product=product, to_product=related_product
                    )

            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to add product. Please ensure the form is valid.'
            )
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """Edit a product in the store"""

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save(commit=False)
            product.save()

            # Update related products
            related_products = form.cleaned_data.get('related_products')
            RelatedProduct.objects.filter(from_product=product).delete()
            if related_products:
                for related_product in related_products:
                    RelatedProduct.objects.create(
                        from_product=product, to_product=related_product
                    )
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to update product. Please ensure the form is valid.'
            )
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """Delete a product from the store"""

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
