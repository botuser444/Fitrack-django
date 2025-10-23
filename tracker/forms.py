from django import forms
from .models import Workout, Meal, Weight, Profile

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = '__all__'

class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = '__all__'

class WeightForm(forms.ModelForm):
    class Meta:
        model = Weight
        fields = '__all__'

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'name',
            'age',
            'height_cm',
            'daily_calorie_goal',
            'water_goal_glasses',
            'bio',
            'profile_picture',  # 🆕 include image upload
        ]
