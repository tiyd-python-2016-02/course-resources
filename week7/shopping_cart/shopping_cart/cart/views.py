from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Category, Product, Cart
from django.views.generic.list import ListView


class CategoryList(ListView):
    model = Category

    context_object_name = 'categories'

# def categories(request):
#     categories = Category.objects.all().order_by('-is_featured')
#
#     context = {"categories" : categories}
#     return render(request, "category/index.html", context)

def show_category(request, cat_id):
    specific_cat = get_object_or_404(Category, id=cat_id)
    context = {"category": specific_cat}
    return render(request, "category/show.html", context)

def add_to_cart(request):
    if request.POST:
        product = Product.objects.get(id=request.POST['product_id'])
        cart, _ = Cart.objects.get_or_create(user=request.user)
        cart.products.add(product)
    return HttpResponseRedirect("/cart")

def show_cart(request):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    context = {"cart": cart}
    return render(request, "category/cart.html", context)
