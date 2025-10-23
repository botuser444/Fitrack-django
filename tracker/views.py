from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from datetime import date
from .models import Workout, Meal, Weight, Profile
from .forms import WorkoutForm, MealForm, WeightForm, ProfileForm

# ----------------- Dashboard -----------------
def dashboard(request):
    today = date.today()
    todays_workouts = Workout.objects.filter(date=today)
    todays_meals = Meal.objects.filter(date=today)
    latest_weight = Weight.objects.order_by('-date').first()

    total_calories = sum(meal.calories for meal in todays_meals)
    workouts_count = todays_workouts.count()

    profile = Profile.objects.first()
    daily_calorie_goal = profile.daily_calorie_goal if profile else 2000
    water_goal_glasses = profile.water_goal_glasses if profile else 8

    context = {
        'todays_workouts': todays_workouts,
        'todays_meals': todays_meals,
        'latest_weight': latest_weight,
        'total_calories': total_calories,
        'workouts_count': workouts_count,
        'profile': profile,
        'daily_calorie_goal': daily_calorie_goal,
        'water_goal_glasses': water_goal_glasses,
    }
    return render(request, 'tracker/dashboard.html', context)


# ----------------- Workouts -----------------
def workout_list(request):
    workouts = Workout.objects.all().order_by('-date')
    return render(request, 'tracker/workout_list.html', {'workouts': workouts})

def workout_add(request):
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Workout added successfully!')
            return redirect('tracker:workout_list')
    else:
        form = WorkoutForm()
    return render(request, 'tracker/workout_form.html', {'form': form, 'action': 'Add'})

def workout_edit(request, pk):
    workout = get_object_or_404(Workout, pk=pk)
    if request.method == 'POST':
        form = WorkoutForm(request.POST, instance=workout)
        if form.is_valid():
            form.save()
            messages.success(request, 'Workout updated successfully!')
            return redirect('tracker:workout_list')
    else:
        form = WorkoutForm(instance=workout)
    return render(request, 'tracker/workout_form.html', {'form': form, 'action': 'Edit'})

def workout_delete(request, pk):
    workout = get_object_or_404(Workout, pk=pk)
    if request.method == 'POST':
        workout.delete()
        messages.success(request, 'Workout deleted successfully!')
        return redirect('tracker:workout_list')
    return render(request, 'tracker/confirm_delete.html', {'object': workout, 'type': 'Workout'})


# ----------------- Meals -----------------
def meal_list(request):
    meals = Meal.objects.all().order_by('-date')
    return render(request, 'tracker/meal_list.html', {'meals': meals})

def meal_add(request):
    if request.method == 'POST':
        form = MealForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Meal added successfully!')
            return redirect('tracker:meal_list')
    else:
        form = MealForm()
    return render(request, 'tracker/meal_form.html', {'form': form, 'action': 'Add'})

def meal_edit(request, pk):
    meal = get_object_or_404(Meal, pk=pk)
    if request.method == 'POST':
        form = MealForm(request.POST, instance=meal)
        if form.is_valid():
            form.save()
            messages.success(request, 'Meal updated successfully!')
            return redirect('tracker:meal_list')
    else:
        form = MealForm(instance=meal)
    return render(request, 'tracker/meal_form.html', {'form': form, 'action': 'Edit'})

def meal_delete(request, pk):
    meal = get_object_or_404(Meal, pk=pk)
    if request.method == 'POST':
        meal.delete()
        messages.success(request, 'Meal deleted successfully!')
        return redirect('tracker:meal_list')
    return render(request, 'tracker/confirm_delete.html', {'object': meal, 'type': 'Meal'})


# ----------------- Weight -----------------
def weight_list(request):
    weights = Weight.objects.all().order_by('date')
    return render(request, 'tracker/weight_list.html', {'weights': weights})

def weight_add(request):
    if request.method == 'POST':
        form = WeightForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Weight entry added successfully!')
            return redirect('tracker:weight_list')
    else:
        form = WeightForm()
    return render(request, 'tracker/weight_form.html', {'form': form, 'action': 'Add'})

def weight_edit(request, pk):
    entry = get_object_or_404(Weight, pk=pk)
    if request.method == 'POST':
        form = WeightForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            messages.success(request, 'Weight entry updated successfully!')
            return redirect('tracker:weight_list')
    else:
        form = WeightForm(instance=entry)
    return render(request, 'tracker/weight_form.html', {'form': form, 'action': 'Edit'})

def weight_delete(request, pk):
    entry = get_object_or_404(Weight, pk=pk)
    if request.method == 'POST':
        entry.delete()
        messages.success(request, 'Weight entry deleted successfully!')
        return redirect('tracker:weight_list')
    return render(request, 'tracker/confirm_delete.html', {'object': entry, 'type': 'Weight'})


# ----------------- Profile -----------------
def profile(request):
    """Create or update the single Profile instance used by the app."""
    profile_instance = Profile.objects.first()
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile_instance)  # <-- added request.FILES
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile saved successfully!')
            return redirect('tracker:dashboard')
    else:
        form = ProfileForm(instance=profile_instance)
    return render(request, 'tracker/profile.html', {'form': form, 'profile': profile_instance})
