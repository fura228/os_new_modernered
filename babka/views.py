from django.shortcuts import render
from django.http import *
from django.template.loader import render_to_string
from .models import Tovar

def page_not_found(request, exception):
    return HttpResponseNotFound('<h1> Page not found </h1>')


def index(request: HttpRequest):
    data = {
        'header_title': "Главная страница",
        'body_title': "Список товаров",
        'tovars': Tovar.objects.all(),
    }
    return render(request, 'babka/index.html', data)



def categories(request, tovar_id):
    tovar = Tovar.objects.all()
    return HttpResponse(f"<h1>{tovar[tovar_id].title}</h1>"
                        f"<p>{tovar[tovar_id].body}</p>"
                        f" Цена: {tovar[tovar_id].cost} руб.</p>")

def about(request: HttpRequest):
    data = {
        'header_title': "О нас",
        'body_title': "О сайте",
        "contacts": [
            {"user": "Начальник", "phone": "+7(800)555-35-35", "email": "principal@yandex.ru"},
            {"user": "Секретарь", "phone": "+7(800)800-80-80", "email": "security@yandex.ru"},
            {"user": "Админ", "phone": "+7(900)000-00-01", "email": "admin@yandex.ru"}
        ]
    }
    return render(request, 'babka/about.html', data)
