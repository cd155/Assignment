from django.shortcuts import render


def home(request):
    return render(request, 'index.html', {'board_n': range(0, 3),
                                          'news_n': range(0, 4)})


def team(request, pk):
    return render(request, 'team.html', {})


def player(request, pk):
    return render(request, 'player.html', {})
