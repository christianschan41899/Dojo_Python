from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, TravelTrip
import bcrypt

#Login and Registration methods
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
        return redirect('/dashboard')

def login(request):
    login_attempt = User.objects.filter(email = request.POST['login_email'])
    if login_attempt:
        logged_user = login_attempt[0]
        if bcrypt.checkpw(request.POST['login_pword'].encode(), logged_user.password.encode()):
            request.session['user_id'] = logged_user.id
            return redirect('/dashboard')
    
    messages.error(request, "Login attempt failed! Email or password is incorrect")
    return redirect('/')

def logout(request):
    try:
        del request.session['user_id']
    except:
        print('No user logged in!')
    
    return redirect('/')

#Trip Buddy Methods
def tripDashboard(request):
    if not 'user_id' in request.session:
        return redirect('/')
    current_user = User.objects.get(id = request.session['user_id'])
    context = {
        "current_user" : current_user,
        #We only want the current user's trips, so use the related name.
        "user_trips" : current_user.trips.all()
    }
    return render(request, 'tripDashboard.html', context)

def createTripForm(request):
    if not 'user_id' in request.session:
        return redirect('/')
    context = {
        "current_user" : User.objects.get(id = request.session['user_id']),
    }
    return render(request, 'createTripForm.html', context)

def createTrip(request):
    if not 'user_id' in request.session:
        return redirect('/')

    errors = TravelTrip.objects.trip_validator(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/trips/new')
    else:
        current_user = User.objects.get(id = request.session['user_id'])
        TravelTrip.objects.create(
            destination = request.POST['dest'],
            plan = request.POST['plan'],
            start_date = request.POST['start'],
            end_date = request.POST['end'],
            users = current_user
        )
        
        return redirect('/dashboard')
    
def viewTrip(request, tripID):
    if not 'user_id' in request.session:
        return redirect('/')
    
    context = {
        "current_user" : User.objects.get(id = request.session['user_id']),
        "current_trip" : TravelTrip.objects.get(id = tripID)
    }

    return render(request, "tripDisplay.html", context)

def tripEditForm(request, tripID):
    if not 'user_id' in request.session:
        return redirect('/')
    
    context = {
        "current_user" : User.objects.get(id = request.session['user_id']),
        "current_trip" : TravelTrip.objects.get(id = tripID)
    }

    return render(request, "editTripForm.html", context)

def editTrip(request, tripID):
    if not 'user_id' in request.session:
        return redirect('/')
    
    errors = TravelTrip.objects.trip_validator(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/trips/edit/'+ str(tripID))
    else:
        editing_trip = TravelTrip.objects.get(id = tripID)
        editing_trip.destination = request.POST['dest']
        editing_trip.plan = request.POST['plan']
        editing_trip.start_date = request.POST['start']
        editing_trip.end_date = request.POST['end']
        editing_trip.save()

        return redirect('/dashboard')

def deleteTrip(request, tripID):
    if not 'user_id' in request.session:
        return redirect('/')
    
    to_delete = TravelTrip.objects.get(id = tripID)
    to_delete.delete()

    return redirect('/dashboard')
    
    