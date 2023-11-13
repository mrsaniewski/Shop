from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm
from django.contrib.auth import logout, login, authenticate

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
    request.session['cart_count'] = request.session.get('cart_count', 0)

    cart = request.session.get('cart', [])
    cart.append(product_id)
    request.session['cart'] = cart

    product_count_key = f'product_{product_id}_count'
    request.session[product_count_key] = request.session.get(product_count_key, 0) + 1

    product = get_object_or_404(Product, pk=product_id)
    product.number -= 1
    product.save()

    request.session['cart_count'] += 1

    return redirect('cart')


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
    for product in products_in_cart:
        product.count_in_cart = response.session.get(f'product_{product.id}_count', 0)
    total_price = sum(product.price * product.count_in_cart for product in products_in_cart)
    return render(response, "main/cart.html", {'products_in_cart': products_in_cart, 'total_price': total_price,
                                               'cart_count': len(cart_ids)})


def remove_from_cart(request, product_id):
    if 'cart' in request.session:
        cart_ids = request.session['cart']
        if product_id in cart_ids:
            product = get_object_or_404(Product, pk=product_id)

            product.number += 1
            product.save()

            product_count_key = f'product_{product_id}_count'
            request.session[product_count_key] = request.session.get(product_count_key, 0) - 1

            request.session['cart_count'] -= 1

            cart_ids.remove(product_id)
            request.session['cart'] = cart_ids

    return redirect('cart')


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect("/home")
    else:
        form = RegisterForm()

    return render(response, "main/register.html", {"form": form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Nieprawidłowe dane logowania.')
    return render(request, "main/home.html")


def logout_view(request):
    logout(request)
    return render(request, "main/home.html")
