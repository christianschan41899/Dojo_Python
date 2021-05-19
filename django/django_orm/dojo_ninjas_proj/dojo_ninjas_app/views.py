from django.shortcuts import render, redirect
from .models import Dojo, Ninja

def home(request):
    context = {
        "all_dojos": Dojo.objects.all()
    }
    return render(request, 'dojo_ninja_display.html', context)

def create_dojo(request):
    if(request.POST['which_form'] == "dojo"):
        postedName = request.POST['inputName']
        postedCity = request.POST['inputCity']
        postedState = request.POST['inputState']
        Dojo.objects.create(name = postedName, city = postedCity, state = postedState, desc = "I'm a dojo!")
    return redirect('/')

def create_ninja(request):
    if(request.POST['which_form'] == "ninja"):
        postedFName = request.POST['input_firstName']
        postedLName = request.POST['input_lastName']
        #For some reason HTML forms can't pass Python classes as values (Just returns Dojo, even though a class should be passed in as a value). Had to settle for their unique IDs instead
        postedDojoID = request.POST['dojoSelect']
        Ninja.objects.create(dojo = Dojo.objects.get(id=postedDojoID), first_name = postedFName, last_name = postedLName)
    return redirect('/')
# Create your views here.
