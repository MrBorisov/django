from django.shortcuts import render

from mainapp.models import Product, ProductCategory


def main(request):
    context = {
        'page_title': 'главная',
        'cl_menu_main': 'active',
    }
    return render(request, 'mainapp/index.html', context)


def products(request, pk=None):
    print(pk)
    product_1 = Product.objects.all()[0]
    menu_prod = ProductCategory.objects.all()
    context = {
        'page_title': 'продукты',
        'cl_menu_prod': 'active',
        'product_1': product_1,
        'menu_prod': menu_prod,
    }
    return render(request, 'mainapp/products.html', context)


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
         'addres': 'Ленинская'}
    ]

    context = {
        'page_title': 'контакты',
        'cl_menu_contacts': 'active',
        'contacts': contacts,
    }
    return render(request, 'mainapp/contact.html', context)
