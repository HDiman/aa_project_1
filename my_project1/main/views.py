from django.shortcuts import render

# Create your views here.
def index(request):
    data = {
        'title': 'Главная страница',
    }
    return render(request, 'news/index.html', data)

def about(request):
    data = {
        'info': 'Информация о нашей компании',
    }
    return render(request, 'news/about.html', data)

