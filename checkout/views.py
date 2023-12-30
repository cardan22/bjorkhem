from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    """ View function for the checkout page."""
    
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51ODRGID60gEJ1KcVUZz1wY2ieofoVFxnoAJaWUAU9Q3MtyDo7eb47haHzQOjc46eCi3NdatxBbwEjCWNi32txhEO00VB2c9VPs',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)


