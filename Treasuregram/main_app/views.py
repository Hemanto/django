from django.shortcuts import render

# Create your views here.


def index(request):
    name = 'gold'
    value = '1233'
    context = {
        'world': name,
        'page': value
    }
    return render(request, 'index.html', context)
