from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('destroy_session', views.destroy)
]