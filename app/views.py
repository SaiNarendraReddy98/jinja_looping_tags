from django.shortcuts import render

# Create your views here.

def for_loop(request):
    d={'Name':'Narendra','sport':'cricket',}


    return render(request,'for_loop.html',d)