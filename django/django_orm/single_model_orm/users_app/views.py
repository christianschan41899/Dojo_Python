from django.shortcuts import render, redirect
from .models import User

def home(request):
    context = {
        "all_users": User.objects.all()
    }
    return render(request, "home.html", context)
# Create your views here.

def register_user(request):
    user_age = request.POST['input_age']
    user_firstname = request.POST['input_firstname']
    user_lastname = request.POST['input_lastname']
    user_email = request.POST['input_email']
    request.session['invalid_input'] = False

    User.objects.create(first_name = user_firstname, last_name = user_lastname, email_address = user_email, age = user_age)
    
    return redirect('/')
    
