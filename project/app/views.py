from django.shortcuts import render


def index(request):
    header = 'Данные пользователя'
    langs = ('Alabuga Polytech')
    group = ('3327A')
    profession = ('Прогромист на языка Python')
    address = ('Прогроммистом')

    data = {'header': header, 'langs':  langs, 'group': group, 'profession': profession , 'address': address}
    return render(request, 'index.html', context=data)


def about(request):
    name = ('Мустафин Адель Ринатович')
    height = ('176cm')
    weight = ('54кг')
    age = ('17лет')

    data = {'name': name, 'height': height, 'weight': weight, 'age': age}
    return render(request, 'about.html', context=data)


def contacts(request):
    number_phone = (89968458038)
    email = ('m_adel_r_2006@mail.ru')
    telegram = ('@WHOMUSTAFA')

    data = {'number_phone': number_phone, 'email': email, 'telegram': telegram}
    return render(request, 'contacts.html', context=data)


def conect(request):
    return render(request, 'conect.html')