from django.shortcuts import render

from catalog.models import Category, Product


def home(request):
    context = {
        'object_list': Product.objects.all(),
        'title': 'Наш ассортимент'
    }
    return render(request, 'catalog/home.html', context)


def contacts(request):
    return render(request, 'catalog/contacts.html')


def goods(request):
    context = {
        'object_list': Product.objects.all(),
        'title': 'Наши товары'
    }
    return render(request, 'catalog/goods.html', context)


def category_stuff(request, pk):
    category_item = Category.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(category_id=pk),
        'title': f'{category_item.name}'
    }
    return render(request, 'catalog/stuff.html', context)

