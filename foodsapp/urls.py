from django.urls import path
from . import views

app_name = "foodsapp"

urlpatterns = [
    path('allfoods/', views.allfoods, name='allfoods'),
    # path('add-food/', views.add_food, name='add_food'),
    path('food/<int:id>/', views.Food_details, name='food_details'),
]
