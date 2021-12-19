from django.shortcuts import render

def index(request):
    title = 'Главная страничка'
    context = {
        'title': title
    }

    return render(request, 'templates/geekshop/index.html', context=context)

def contacts(request):

    title = 'Контакты'
    context = {
        'title': title
    }
    return render(request, 'templates/geekshop/contacts.html', context=context)