from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.registerPage),
    path('registration', views.register),
    path('login', views.login),
    path('wall', include('comment_wall_app.urls')),
]