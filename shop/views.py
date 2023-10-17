from django.shortcuts import render, redirect
from .forms import RegisterForm

# Create your views here.
from django.http import HttpResponse, response
from .models import Product


def index(response):
    products = Product.objects.all()
    latest_products = Product.objects.order_by('-id')[:5]
    return render(response, "main/home.html", {"products": products, 'latest_products': latest_products})


def tapes(response):
    products = Product.objects.filter(category=0)
    return render(response, "main/tapes.html", {"products": products})


def add_to_cart(request, product_id):
    request.session['cart'] = request.session.get('cart', []) + [product_id]
    return redirect('tapes')


def glues(response):
    products = Product.objects.filter(category=1)
    return render(response, "main/glues.html", {"products": products})


def grids(response):
    products = Product.objects.filter(category=2)
    return render(response, "main/grids.html", {"products": products})


def gloves(response):
    products = Product.objects.filter(category=3)
    return render(response, "main/gloves.html", {"products": products})


def contact(response):
    return render(response, "main/contact.html")


def about(response):
    return render(response, "main/about.html")


def cart(response):
    cart_ids = response.session.get('cart', [])
    products_in_cart = Product.objects.filter(id__in=cart_ids)
    total_price = sum(product.price * product.number for product in products_in_cart)
    return render(response, "main/cart.html", {'products_in_cart': products_in_cart, 'total_price': total_price})


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect("/home")
    else:
        form = RegisterForm()

    return render(response, "main/register.html", {"form": form})
