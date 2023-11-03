from django.shortcuts import render


def home(request):
    speakers = [
        {'name': 'Grace Hopper', 'photo': 'https://cleberfonseca.com.br/img/hopper.jpeg'},
        {'name': 'Alan Turing', 'photo': 'https://cleberfonseca.com.br/img/turing.jpeg'}
    ]
    return render(request, 'index.html', {'speakers': speakers})
