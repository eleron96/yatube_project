from django.http import HttpResponse
from django.shortcuts import render
# Импортируем модель, чтобы обратиться к ней
from .models import Post

# Create your views here.


def index(request):
    # Одна строка вместо тысячи слов на SQL:
    # в переменную posts будет сохранена выборка из 10 объектов модели Post,
    # отсортированных по полю pub_date по убыванию (от больших значений к меньшим)
    posts = Post.objects.order_by('-pub_date')[:10]
    # В словаре context отправляем информацию в шаблон
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


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
