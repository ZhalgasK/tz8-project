from django.shortcuts import render, get_object_or_404
from .models import Category, Store

def home(request, category_slug=None):
    category_page = None
    stores = None
    if category_slug != None:
        category_page = get_object_or_404(Category, slug = category_slug)
        stores = Store.objects.filter(category = category_page, available = True)
    else:
        stores = Store.objects.all().filter(available = True)
    return render(request, 'shop/home.html', {'category': category_page, 'stores': stores})

def store(request):
    return render(request, 'shop/store.html')





# Create your views here.
