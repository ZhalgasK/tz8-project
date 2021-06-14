from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<slug:category_slug>', views.home, name='stores_by_category'),
    path('store/', views.store, name='store'),
]
