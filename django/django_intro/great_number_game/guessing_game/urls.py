from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('determine', views.check),
    path('destroy', views.destroy_session)
]