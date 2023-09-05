from django.shortcuts import render


def home(request):
    return render(request, 'index.html', {'board_n': range(0, 3),
                                          'news_n': range(0, 4)})
