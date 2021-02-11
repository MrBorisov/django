import random

from django.shortcuts import render, get_object_or_404

from mainapp.models import Product, ProductCategory


def get_menu():
    return ProductCategory.objects.all()


def get_hot_product():
    product_ids = Product.objects.values_list('id', flat=True).all()
    rnd_id = random.choice(product_ids)
    return Product.objects.get(pk=rnd_id)


def same_products(hot_product):
    return Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk)[:3]


def main(request):
    context = {
        'page_title': 'главная',

    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    hot_product = get_hot_product()
    context = {
        'page_title': 'продукты',
        'hot_product': hot_product,
        'menu_prod': get_menu(),
        'same_products': same_products(hot_product),
    }
    return render(request, 'mainapp/products.html', context)


def category(request, pk):
    if pk == 0:
        category = {'pk': 0, 'name': 'все'}
        products = Product.objects.all()
    else:
        category = get_object_or_404(ProductCategory, pk=pk)
        products = category.product_set.all()
    context = {
        'page_title': 'товары категории',
        'category': category,
        'products': products,
        'menu_prod': get_menu(),
    }
    return render(request, 'mainapp/category_products.html', context)


def product_page(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'page_title': 'Страница продукта',
        'product': product,
        'menu_prod': get_menu(),

    }
    return render(request, 'mainapp/product_page.html', context)


def contact(request):
    contacts = [
        {'city': 'Владивосток',
         'phone': '+9644444555',
         'email': 'mail@mail.ru',
         'addres': 'Океанский пр-т'},
        {'city': 'Находка',
         'phone': '+9644444444',
         'email': 'mail1@mail.ru',
         'addres': 'Ленинская'},
        {'city': 'Хабаровск',
         'phone': '+9644444333',
         'email': 'mail2@mail.ru',
         'addres': 'Карла Маркса'}
    ]

    context = {
        'page_title': 'контакты',
        'cl_menu_contacts': 'active',
        'contacts': contacts,
    }
    return render(request, 'mainapp/contact.html', context)
