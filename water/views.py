from django.shortcuts import render
from django.utils import timezone
from .models import Grundwasserstand

def wasserstand_list(request):
    wasserstand = Grundwasserstand.objects.all()
    print("*"*100)
    print(wasserstand)
    print("*"*100)
    return render(request,'water/wasserstand_list.html', {'stands': wasserstand})
