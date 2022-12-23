from django.contrib import admin
from .models import Exercise, Workout, WorkoutExercise, DailyWorkout, User, FavoriteWorkout, UserExercise

all_models = [Exercise, Workout, WorkoutExercise, DailyWorkout, User, FavoriteWorkout, UserExercise]
# Register your models here.
admin.site.register(all_models)
