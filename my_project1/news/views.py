from django.shortcuts import render

# Create your views here.
def news_home(request):
    data = {
        'title': 'Yahoo News',
    }
    return render(request, 'news/index.html', data)
