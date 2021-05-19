from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path('shows', views.tvShowList),
    path('shows/new', views.newShow),
    path('shows/create', views.createShow),
    path('shows/<int:show_id>', views.tvShowDisplay),
    path('shows/<int:show_id>/edit', views.tvShowEditForm),
    path('shows/<int:show_id>/update', views.tvShowUpdate),
    path('shows/<int:show_id>/destroy', views.tvShowDestroy),
]
