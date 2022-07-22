from django.contrib import admin
from .models import Exercise, Workout, WorkoutExercise, DailyWorkouts, User

all_models = [Exercise, Workout, WorkoutExercise, DailyWorkouts, User]
# Register your models here.
admin.site.register(all_models)
