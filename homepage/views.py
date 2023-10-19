from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import logout
from django.urls import reverse
from django.shortcuts import redirect
from django.db import IntegrityError
from homepage.models import User, Product, Purchase, ShoppingCart
from.forms import ProductForm
from .util import bestsell
from django.shortcuts import get_object_or_404

def homepage(request):
    users = User.objects.all()
    bestsell_ids = bestsell(Purchase.objects.all())
    number_products = 6
    products = Product.objects.filter(id__in=bestsell_ids)[:number_products]
    product_id_to_order = {product_id: order for order, product_id in enumerate(bestsell_ids)}
    products = sorted(products, key=lambda product: product_id_to_order[product.id])
    return render(request, 'homepage.html', {'products': products})


def login_user(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("homepage:homepage"))
        else:
            return render(request, "login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "login.html")


def logout_user(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('homepage:homepage')

def register_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("homepage:login"))
    else:
        return render(request, "register.html")
    
def products(request):
    products = Product.objects.all()
    return render(request, "products.html", {'products': products})


def basket(request):
    user = request.user
    shopping_cart = ShoppingCart.objects.filter(user=user).first()
    print(shopping_cart)
    return render(request, "basket.html", {'cart' : shopping_cart})

def category_games(request, category):
    products = Product.objects.filter(category=category)
    return render(request, "products.html", {'products': products})

def product_info(request, product_id):
    product = Product.objects.get(id=product_id)
    print(product.name)
    return render(request, "product_info.html", {'product': product})