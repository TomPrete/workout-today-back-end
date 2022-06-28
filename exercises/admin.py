from django.contrib import admin
from .models import Exercise, Workout, WorkoutExercise, DailyWorkouts

all_models = [Exercise, Workout, WorkoutExercise, DailyWorkouts]
# Register your models here.
admin.site.register(all_models)
