from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.registerPage),
    path('registration', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('dashboard', views.tripDashboard),
    path('trips/new', views.createTripForm),
    path('add_trip', views.createTrip),
    path('trips/<int:tripID>', views.viewTrip),
    path('trips/edit/<int:tripID>', views.tripEditForm),
    path('edit_trip/<int:tripID>', views.editTrip),
    path('delete/<int:tripID>', views.deleteTrip)
]