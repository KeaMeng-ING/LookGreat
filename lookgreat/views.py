
from django.shortcuts import render

from store.models import Product
from orders.models import OrderProduct

# def home(request):
#     products = Product.objects.all().filter(is_available=True)
#     # Popular Products Get from OrderProduct
#     # products = OrderProduct.objects.all().filter(ordered=True)
#     context = {
#         'products': products,
#     }
#     return render(request, 'home.html', context)

from django.db.models import Count

def home(request):
    # Get products ordered by popularity (number of times they've been ordered)
    products = OrderProduct.objects.values('product').annotate(ordered_count=Count('product')).order_by('-ordered_count')

    # Get the actual Product instances
    products = [Product.objects.get(id=item['product']) for item in products if Product.objects.filter(id=item['product'], is_available=True).exists()]

    context = {
        'products': products,
    }
    return render(request, 'home.html', context)