from django.shortcuts import render, redirect
from django.contrib.auth import login

from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import ProductForm
from .forms import SignUpForm

@login_required
def create_product(request):
    print(request)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.creator = request.user  # Assign current user as creator
            product.save()
            return redirect("product_list")
    else:
        form = ProductForm()

    return render(request, "dndstores/create_product.html", {"form": form})
    
def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the new user
            return redirect("home")  # Change this to your home page
    else:
        form = SignUpForm()

    return render(request, "dndstores/signup.html", {"form": form})

def home(request):
    return render(request, "dndstores/home.html")  # Create a home.html template
