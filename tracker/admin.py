from django.contrib import admin
from .models import Workout, Meal, Weight, Profile

@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('exercise_name', 'date', 'sets', 'reps', 'weight')
    list_filter = ('exercise_name', 'date')
    search_fields = ('exercise_name', 'notes')

@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ('meal_name', 'meal_type', 'date', 'calories')
    list_filter = ('meal_type', 'date')
    search_fields = ('meal_name',)

@admin.register(Weight)
class WeightAdmin(admin.ModelAdmin):
    list_display = ('weight', 'date')
    ordering = ('-date',)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'height_cm', 'daily_calorie_goal', 'water_goal_glasses')
    search_fields = ('name',)
