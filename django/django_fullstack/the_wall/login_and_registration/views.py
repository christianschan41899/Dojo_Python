from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import bcrypt

def registerPage(request):
    return render(request, 'registrationPage.html')

def register(request):
    errors = User.objects.register_validator(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        pword = request.POST['pword']
        pw_hash = bcrypt.hashpw(pword.encode(), bcrypt.gensalt()).decode()
        User.objects.create(
            first_name=request.POST['fName'], 
            last_name=request.POST['lName'], 
            email = request.POST['email'],
            password=pw_hash)
        request.session['user_id'] = User.objects.last().id
        return redirect('/wall')

def login(request):
    login_attempt = User.objects.filter(email = request.POST['login_email'])
    if login_attempt:
        logged_user = login_attempt[0]
        if bcrypt.checkpw(request.POST['login_pword'].encode(), logged_user.password.encode()):
            request.session['user_id'] = logged_user.id
            return redirect('/wall')
    
    messages.error(request, "Login attempt failed! Email or password is incorrect")
    return redirect('/')

