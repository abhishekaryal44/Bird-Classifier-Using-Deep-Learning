from django.urls import path
from home import views
from . import views


urlpatterns = [
    path('', views.abhishek, name='abhishek'),
    path('home/', views.renderHome, name='renderHome'),  # Added a slash here and a comma after the line
    path('add_bird_species/', views.add_bird_species, name='add_bird_species'),  
    path('species_detail/<int:species_id>/', views.species_detail, name='species_detail'),
]
