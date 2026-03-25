from django.shortcuts import render, redirect
from .models import Kruzok
from .forms import KruzokForm
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

def pridaj_kruzok(request):
    if request.method == "POST":
        form = KruzokForm(request.POST)
        if form.is_valid():
            form.save()
            #return redirect('index')  # presmerujeme späť na hlavný zoznam
    else:
        form = KruzokForm()
    
    return render(request, 'kruzky/pridaj_kruzok.html', {'form': form})