from django.shortcuts import render
from .models import Kruzok

def index(request):
    order = {
        "Pondelok": 1,
        "Utorok": 2,
        "Streda": 3,
        "Štvrtok": 4,
        "Piatok": 5,
        "Sobota": 6,
        "Nedeľa": 7,
    }

    kruzky = sorted(
        Kruzok.objects.all(),
        key=lambda k: order.get(k.den, 99)
    )

    return render(request, 'kruzky/index.html', {'kruzky': kruzky})