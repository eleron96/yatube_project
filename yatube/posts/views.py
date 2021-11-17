from django.http import HttpResponse


# Create your views here.


def index(request):
    return HttpResponse('Главная страница')


def posts_list(request):
    return HttpResponse('Список постов')


def group_posts(request, slug):
    return HttpResponse(f'Пост номер {slug}')