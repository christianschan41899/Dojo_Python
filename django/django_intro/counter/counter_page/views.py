from django.shortcuts import render, redirect

def home(request):
    if ('visits' in request.session):
        request.session['visits'] = request.session['visits'] + 1
    else:
        request.session['visits'] = 1
    return render(request, 'counter.html')

def destroy(request):
    try:
        del request.session['visits']
    except:
        print("Key does not exist yet!")
    
    return redirect('/')
