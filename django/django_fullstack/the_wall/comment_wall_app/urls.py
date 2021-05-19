from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.commentWallDisplay),
    path('/makeMessage', views.createMessage),
    path('/comment', views.createComment),
    path('/destroy', views.logout)
]