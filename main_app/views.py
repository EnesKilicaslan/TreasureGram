from django.shortcuts import render
#from django.http import HttpResponse



# Create your views here.

def index(request):
    return render(request, 'index.html', {'treasures': treasures})


class Treasure:
    def __init__(self, name, value, material, location):
        self.name = name
        self.value = value
        self.material = material
        self.location = location


treasures = [
        Treasure('Gold Nugget', 240, 'Gold', 'LA'),
        Treasure('Fools\' Gold', 130, 'pyrite', 'San Diego'),
        Treasure('Coffee Can', 20.0, 'tin', 'CA')
]







