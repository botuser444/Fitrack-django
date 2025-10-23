# tracker/urls.py
from django.urls import path
from . import views

app_name = 'tracker'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    # Workouts
    path('workouts/', views.workout_list, name='workout_list'),
    path('workouts/add/', views.workout_add, name='workout_add'),
    path('workouts/<int:pk>/edit/', views.workout_edit, name='workout_edit'),
    path('workouts/<int:pk>/delete/', views.workout_delete, name='workout_delete'),

    # Meals
    path('meals/', views.meal_list, name='meal_list'),
    path('meals/add/', views.meal_add, name='meal_add'),
    path('meals/<int:pk>/edit/', views.meal_edit, name='meal_edit'),
    path('meals/<int:pk>/delete/', views.meal_delete, name='meal_delete'),

    # Weight
    path('weight/', views.weight_list, name='weight_list'),
    path('weight/add/', views.weight_add, name='weight_add'),
    path('weight/<int:pk>/edit/', views.weight_edit, name='weight_edit'),
    path('weight/<int:pk>/delete/', views.weight_delete, name='weight_delete'),

    # Profile
    path('profile/', views.profile, name='profile'),
]
