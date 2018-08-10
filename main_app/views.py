from django.shortcuts import render
#from django.http import HttpResponse
from .models import Treasure


# Create your views here.

def index(request):
    treasures = Treasure.objects.all()
    return render(request, 'index.html', {'treasures': treasures})

treasures = [
        Treasure('Gold Nugget', 240, 'Gold', 'LA'),
        Treasure('Fools\' Gold', 130, 'pyrite', 'San Diego'),
        Treasure('Coffee Can', 20.0, 'tin', 'CA')
]







