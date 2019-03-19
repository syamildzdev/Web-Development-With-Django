from django.shortcuts import render
from .models import Beverage # the dot . is because models.py is placed in current directory

def home(request):
    context = {
        'beverages': Beverage.objects.all()
    }
    return render(request, 'cafe/home.html', context)


def about(request):
    return render(request, 'cafe/about.html', {'title': 'About'})
