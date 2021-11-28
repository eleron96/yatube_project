from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def index(request):
    template = 'posts/index.html'
    title = 'Главная страница'
    context = {
        # В словарь можно передать переменную
        'title': title,
        # А можно сразу записать значение в словарь. Но обычно так не делают
        'text': 'Главная страница',
    }
    return render(request, template, context)


def posts_list(request):
    template = 'posts/group_list.html'
    title = 'Листы постов'
    context = {
        # В словарь можно передать переменную
        'title': title,
        # А можно сразу записать значение в словарь. Но обычно так не делают
        'text': f'{title} будут отображенны на этой странице',
    }
    return render(request, template, context)


def group_posts(request):
    template = 'posts/group_posts.html'
    title = 'Посты групп'
    context = {
        # В словарь можно передать переменную
        'title': title,
        # А можно сразу записать значение в словарь. Но обычно так не делают
        'text': f'на данной странице будут отображены {title}',
    }
    return render(request, template, context)
