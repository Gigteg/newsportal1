from django.shortcuts import render
from hashlib import md5
from datetime import datetime
from .models import User

# Create your views here.

data = dict()

def get_user(request):
    global data
    if 'user' in request.session:
        user = request.session['user']
    else:
        user = 'Гость'
    data['user'] = user


def signup(request):
    global data
    get_user(request)
    """ Форма регистрации пользователей """
    if request.method == 'GET':
        return render(request, 'account/signup.html', context=data)
    elif request.method == 'POST':

        # ИЗВЛЕЧЕНИЕ ДАНЫХ:
        login = request.POST.get('login')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        # СОЗДАНИЕ НАБОРА ДАННЫХ
        data = dict()
        data['report'] = 'Отчет по умолчанию'

        # ПРОВЕРКА СОВПАДЕНИЯ ПАРОЛЕЙ
        if pass1 != pass2:
            data['report'] = 'Пароли не совпадают!'
        else:
            # ХЕШИРОВАНИЕ ПАРОЛЯ
            _byte = pass1.encode()
            _hash = md5(_byte)
            passw = _hash.hexdigest()

            # ОПРЕДЕЛЕНИЕ ВРЕМЕНИ РЕГИСТРАЦИИ
            now = datetime.now()
            regdate = datetime.strftime(now, '%Y-%m-%d %H:%M:%S')
            status = 'norm'

            """
            # УПАКОВКА ДАННЫХ (КОНТРОЛЬ ДАННЫХ):
            data['login'] = login
            data['pass1'] = pass1
            data['pass2'] = pass2
            data['email'] = email
            data['passw'] = passw
            data['regdate'] = regdate
            data['status'] = status
            """

            #СОХРАНЕНИЕ ДАННЫХ В БАЗЕ
            new_user = User()
            new_user.login = login
            new_user.passw = passw
            new_user.email = email
            new_user.regdate = regdate
            new_user.status = status
            new_user.save()

            #Result
            data['report'] = 'Регистрация успешно завершена'


        # ОТПРАВКА ДАННЫХ НА СТРАНИЦУ ОТЧЕТА
        return render(request, 'account/signup_res.html', context=data)


def signin(request):
    global data
    get_user(request)
    if request.method == 'GET':
        return render(request, 'account/signin.html', context=data)
    elif request.method == 'POST':
        # data = dict()

        # ИЗВЛЕЧЕНИЕ ДАНЫХ:
        _login = request.POST.get('login')
        _pass1 = request.POST.get('pass1')

        # УПАКОВКА ДАННЫХ (КОНТРОЛЬ ДАННЫХ):
        data['login'] = _login
        data['pass1'] = _pass1

        # ХЕШИРОВАНИЕ ПАРОЛЯ:
        _byte = _pass1.encode()
        _hash = md5(_byte)
        _passw = _hash.hexdigest()

        #ПРОВЕРКА ПОЛЬЗОВАТЕЛЯ
        try:
            user = User.objects.get(login=_login, passw=_passw)
            data['report'] = 'Вы успешно авторизированы!'
            data['x_color'] = 'darkcyan'
            request.session['user'] = _login
        except User.DoesNotExist as err:
            data['report'] = 'Вы ввели неверные имя пользователя или пароль!'
            data['x_color'] = 'red'

        # ЗАГРУЗКА СТРАНИЦЫ ОТЧЕТА
        return render(request, 'account/signin_res.html', context=data)

def signout(request):
    return render(request, 'account/signout.html')


def profile(request):
    return render(request, 'account/profile.html')
