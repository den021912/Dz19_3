from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister

# Create your views here.
def sign_up_by_django(request):
    users = ['Нина', 'Миша', 'Вася', 'Света']
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
                return render(request, 'fifth_task/registration_page.html', context=info)
            elif repeat_password1 != password1:
                info['error'] = 'Пароли не совпадают'
                return render(request, 'fifth_task/registration_page.html', context=info)
            elif int(age1) < 18:
                info['error'] = 'Вы должны быть старше 18'
                return render(request, 'fifth_task/registration_page.html', context=info)
            else:
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                repeat_password = form.cleaned_data['repeat_password']
                age = form.cleaned_data['age']
                info = {}
                return render(request, 'fifth_task/registration_page.html',
                              context={'wellcome': f'Приветствуем, {username1}!'})
    else:
        form = UserRegister()
    return render(request, 'fifth_task/registration_page.html')


def sign_up_by_html(request):
    users = ['Нина', 'Миша', 'Вася', 'Света']
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
                return render(request, 'fifth_task/registration_page.html', context=info)
            elif repeat_password1 != password1:
                info['error'] = 'Пароли не совпадают'
                return render(request, 'fifth_task/registration_page.html', context=info)
            elif int(age1) < 18:
                info['error'] = 'Вы должны быть старше 18'
                return render(request, 'fifth_task/registration_page.html', context=info)
            else:
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                repeat_password = form.cleaned_data['repeat_password']
                age = form.cleaned_data['age']
                info = {}
                return render(request, 'fifth_task/registration_page.html',
                              context={'wellcome': f'Приветствуем, {username1}!'})
    else:
        form = UserRegister()
    return render(request, 'fifth_task/registration_page.html')