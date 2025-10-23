from django.db import models
from django.conf import settings

class Workout(models.Model):
    exercise_name = models.CharField(max_length=200)
    date = models.DateField()
    sets = models.PositiveIntegerField(null=True, blank=True)
    reps = models.PositiveIntegerField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.exercise_name} ({self.date})"


class Meal(models.Model):
    meal_name = models.CharField(max_length=200)
    meal_type = models.CharField(max_length=100)
    calories = models.PositiveIntegerField(default=0)
    protein = models.FloatField(default=0)
    carbs = models.FloatField(default=0)
    fats = models.FloatField(default=0)
    date = models.DateField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.meal_name} ({self.date})"


class Weight(models.Model):
    weight = models.FloatField()
    date = models.DateField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.weight} kg ({self.date})"


# ---------------- Profile model ----------------
class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='profile'
    )
    name = models.CharField(max_length=120, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    height_cm = models.PositiveIntegerField(null=True, blank=True)
    daily_calorie_goal = models.PositiveIntegerField(default=2000)
    water_goal_glasses = models.PositiveIntegerField(default=8)
    bio = models.TextField(blank=True)

    # 🆕 profile picture field
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

    def __str__(self):
        if self.name:
            return self.name
        return f"Profile #{self.pk}"
