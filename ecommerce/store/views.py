from django.shortcuts import render
from .models import *


def store(request):
    products = Product.objects.all()
    context = {"products":products}
    return render(request, 'store/store.html', context)

def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)

def about(request):
    context = {}
    return render(request, 'store/about.html', context)

def contact(request):
    context = {}
    return render(request, 'store/contact.html', context)

def login(request):
    context = {}
    return render(request, 'store/login.html', context)
    
def register(request):
    context = {}
    return render(request, 'store/register.html', context)
    
def dashboard(request):
    context = {}
    return render(request, 'store/dashboard.html', context)
    
def settings(request):
    context = {}
    return render(request, 'store/settings.html', context)