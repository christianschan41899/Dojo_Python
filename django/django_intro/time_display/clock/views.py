from django.shortcuts import render, redirect
from time import gmtime, strftime

def root(request):
    return redirect('/time_display')    

def index(request):
    context = {
        "time": strftime("%A, %B %d, %Y \n %H:%M:%S %p GMT", gmtime())
    }
    return render(request,'time.html', context)

