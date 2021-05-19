from django.urls import path
from . import views

urlpatterns = [
    path('', views.hangar),
    path('create', views.create),
    path('mechlab', views.mechLab)
]