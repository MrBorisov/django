from django.shortcuts import render, get_object_or_404

from mainapp.models import Product, ProductCategory


def get_menu():
    return ProductCategory.objects.all()


def main(request):
    context = {
        'page_title': 'главная',
        'cl_menu_main': 'active',
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    product_1 = Product.objects.all()[0]
    context = {
        'page_title': 'продукты',
        'product_1': product_1,
        'menu_prod': get_menu(),
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
