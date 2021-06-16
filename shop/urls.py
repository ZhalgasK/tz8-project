from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<slug:category_slug>', views.home, name='stores_by_category'),
    path('<slug:category_slug>/<slug:store_slug>', views.store, name='store_detail'),
    path('cart/', views.cart, name='cart'),
]
