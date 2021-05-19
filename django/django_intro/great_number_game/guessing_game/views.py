from django.shortcuts import render, redirect
import random

def home(request):
    if not 'random_number' in request.session:
        request.session['random_number'] = random.randint(1, 100)
    if not 'tries' in request.session:
        request.session['tries'] = 0
    number = request.session['random_number']
    print(f'My random number is {number}')
    return render(request, 'game.html')

def check(request):
    request.session['guess'] = int(request.POST['guess'])
    if(request.session['guess'] == request.session['random_number']):
        request.session['correct'] = True
    else:
        request.session['correct'] = False
    request.session['tries'] = request.session['tries'] + 1
    return redirect('/')

def destroy_session(request):
    try:
        del request.session['random_number']
    except:
        print("Key does not exist yet!")

    try:
        del request.session['guess']
    except:
        print("Key does not exist yet!")
    
    try:
        del request.session['correct']
    except:
        print("Key does not exist yet!")

    try:
        del request.session['tries']
    except:
        print("Key does not exist yet!")

    return redirect('/')
# Create your views here.
