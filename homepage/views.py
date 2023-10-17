from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import logout
from django.urls import reverse
from django.shortcuts import redirect
from django.db import IntegrityError
from homepage.models import User, Product

def homepage(request):
    users = User.objects.all()
    number_products = 4
    products = Product.objects.all()[:number_products]
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
    return render(request, "homepage.html")

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