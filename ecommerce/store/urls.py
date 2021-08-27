from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name="store"),
    path('cart', views.cart, name="cart"),
    path('checkout', views.checkout, name="checkout"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('login', views.login, name="login"),
    path('register', views.register, name="register"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('settings', views.settings, name="settings"),
    path('update_item/', views.updateItem, name="update_item"),
]