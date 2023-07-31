from django.urls import path
from . import views

urlpatterns = [
    path('shows', views.display_all),
    path('shows/new', views.index),
    path('shows/create',views.create_show),
    path('shows/<int:id>', views.display_show),
    path('shows/<int:id>/edit', views.edit_show),
    path('shows/update/<int:id>', views.update),
    path('shows/<int:id>/delete', views.delete),
]   