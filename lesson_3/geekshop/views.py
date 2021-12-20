from django.shortcuts import render

from mainapp.models import Product


def index(request):
    title = 'Главная страничка'

    products = Product.objects.all()
    context = {
        'title': title,
        'products': products,
    }

    return render(request, 'templates/geekshop/index.html', context=context)

def contacts(request):

    title = 'Контакты'
    context = {
        'title': title
    }
    return render(request, 'templates/geekshop/contacts.html', context=context)