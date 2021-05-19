from django.shortcuts import render, redirect
from time import localtime, strftime
import random

def home(request):
    if not 'player_gold' in request.session:
        request.session['player_gold'] =  0
    
    if not 'actions' in request.session:
        request.session['actions'] = []
    
    return render(request, 'game.html')


def process(request):
    choice = request.POST["which_choice"]
    if(choice == "casino"):
        request.session['earnings'] = random.randint(-50, 50)
        request.session['player_gold'] =  request.session['player_gold'] + request.session['earnings']
        if(request.session['earnings']<0):
            request.session['actions'].append(f"<p class = 'red'> Entered a casino and lost {request.session['earnings']} gold. {strftime('%Y/%m/%d %H:%M %p', localtime())} </p>")
        else:
            request.session['actions'].append(f"<p class = 'green'> Entered a casino and earned {request.session['earnings']} gold. {strftime('%Y/%m/%d %H:%M %p', localtime())} </p>")
    elif(choice == "cave"):
        request.session['earnings'] = random.randint(5, 10)
        request.session['player_gold'] =  request.session['player_gold'] + request.session['earnings']
        request.session['actions'].append(f"<p class = 'green'> Earned {request.session['earnings']} gold from the caves! {strftime('%Y/%m/%d %H:%M %p', localtime())} </p>")
    elif(choice == "house"):
        request.session['earnings'] = random.randint(2, 5)
        request.session['player_gold'] =  request.session['player_gold'] + request.session['earnings']
        request.session['actions'].append(f"<p class = 'green'> Earned {request.session['earnings']} gold from the house! {strftime('%Y/%m/%d %H:%M %p', localtime())} </p>")
    elif(choice == "farm"):
        request.session['earnings'] = random.randint(10, 20)
        request.session['player_gold'] =  request.session['player_gold'] + request.session['earnings']
        request.session['actions'].append(f"<p class = 'green'> Earned {request.session['earnings']} gold from the farm! {strftime('%Y/%m/%d %H:%M %p', localtime())} </p>")
    request.session.save()
    return redirect('/')

def reset(request):
    try:
        del request.session['earnings']
        del request.session['player_gold']
        del request.session['actions']
    except:
        print("Key does not exist!")
    request.session.save()
    return redirect('/')
# Create your views here.
