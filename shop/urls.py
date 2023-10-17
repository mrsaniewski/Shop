from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.index, name="index"),
    path("tapes/", views.tapes, name="tapes"),
    path("glues/", views.glues, name="glues"),
    path("grids/", views.grids, name="grids"),
    path("gloves/", views.gloves, name="gloves"),
    path("contact/", views.contact, name="contact"),
    path("about/", views.about, name="about"),
    path("cart/", views.cart, name="cart"),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('register/', views.register, name='register'),
    path('', include("django.contrib.auth.urls")),
]