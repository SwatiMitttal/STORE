from django.urls import path
from . import views

urlpatterns = [
    path('cart/',views.cart,name='cart'),
    path('rem_cart/<int:pid>/',views.rem_cart,name='rem_cart'),
    path('store/cart/',views.cart,name='cart'),
    path('cart/<int:pid>/',views.add_cart,name='add_cart')
]
