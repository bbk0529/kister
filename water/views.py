from django.shortcuts import render

def wasserstand_list(request):
    return render(request,'water/wasserstand_list.html', {})
