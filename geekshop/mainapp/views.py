from django.shortcuts import render

def products(request):

    title = 'Каталог'

    links_menu = [
        {'href': '', 'name': 'Все'},
        {'href': 'products_home', 'name': 'Дом'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_classic', 'name': 'классика'},
    ]
    context = {
        'title': title,
        'links_menu': links_menu,
    }
    return render(request, 'mainapp/products.html', context=context)



