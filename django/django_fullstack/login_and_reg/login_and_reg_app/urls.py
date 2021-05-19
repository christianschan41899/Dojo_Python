from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.registerPage),
    path('registration', views.register),
    path('login', views.login),
    path('success', views.successfulLogin),
    path('logout', views.logout)
]
