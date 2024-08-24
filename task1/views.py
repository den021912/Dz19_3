from django.shortcuts import render
from task1.forms import UserRegister
from .models import Game, Buyer


# Create your views here.

def class_template(request):
    title_class_template = 'Магазин'
    context = {
        'title_class_template': title_class_template
    }
    return render(request, 'class_template.html', context=context)


def games(request):
    title_games = 'Игры'
    buy = 'Купить'
    gamess = Game.objects.all()
    context = {
        'title_games': title_games,
        'buy': buy,
        'gamess': gamess
    }
    return render(request, "games.html", context=context)


def basket(request):
    title_basket = 'Корзина'
    context = {
        'title_basket': title_basket,
    }
    return render(request, "basket.html", context=context)


def menu(request):
    magazine = 'Магазин'
    mane_page = 'Главная страница'
    magazine_page = 'Яндекс'
    basket_page = 'Корзина'
    context = {
        'magazine': magazine,
        'mane_page': mane_page,
        'magazine_page': magazine_page,
        'basket_page': basket_page
    }
    return render(request, "menu.html", context=context)


def sign_up_by_django(request):
    buyers = Buyer.objects.all()
    users = set()
    for buyer in buyers:
        users.add(buyer.name)
    info = {}
    len_info = len(info)
    if request.method == 'POST':
        form = UserRegister(request.POST)
        username1 = request.POST.get('username')
        password1 = request.POST.get('password')
        repeat_password1 = request.POST.get('repeat_password')
        age1 = request.POST.get('age')
        if form.is_valid():
            if username1 in users:
                info['error'] = 'Пользователь уже существует'
                return render(request, 'registration_page.html', context=info)
            elif repeat_password1 != password1:
                info['error'] = 'Пароли не совпадают'
                return render(request, 'registration_page.html', context=info)
            elif int(age1) < 18:
                info['error'] = 'Вы должны быть старше 18'
                return render(request, 'registration_page.html', context=info)
            else:
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                repeat_password = form.cleaned_data['repeat_password']
                age = form.cleaned_data['age']
                Buyer.objects.create(name=username, balance=0, age=age)
                info = {}
                return render(request, 'registration_page.html',
                              context={'wellcome': f'Приветствуем, {username1}!'})
    else:
        form = UserRegister()
    return render(request, 'registration_page.html')


def sign_up_by_html(request):
    buyers = Buyer.objects.all()
    users = set()
    for buyer in buyers:
        users.add(buyer.name)
    info = {}
    len_info = len(info)
    if request.method == 'POST':
        form = UserRegister(request.POST)
        username1 = request.POST.get('username')
        password1 = request.POST.get('password')
        repeat_password1 = request.POST.get('repeat_password')
        age1 = request.POST.get('age')
        if form.is_valid():
            if username1 in users:
                info['error'] = 'Пользователь уже существует'
                return render(request, 'registration_page.html', context=info)
            elif repeat_password1 != password1:
                info['error'] = 'Пароли не совпадают'
                return render(request, 'registration_page.html', context=info)
            elif int(age1) < 18:
                info['error'] = 'Вы должны быть старше 18'
                return render(request, 'registration_page.html', context=info)
            else:
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                repeat_password = form.cleaned_data['repeat_password']
                age = form.cleaned_data['age']
                Buyer.objects.create(name=username, balance=0, age=age)
                info = {}
                return render(request, 'registration_page.html',
                              context={'wellcome': f'Приветствуем, {username1}!'})
    else:
        form = UserRegister()
    return render(request, 'registration_page.html')

