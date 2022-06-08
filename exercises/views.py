from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View

from exercises.serializers import ExerciseSerializer
from .workout_generator import get_exercises_for_workout, no_repeat_target_muscle
from exercises.models import Exercise, Workout, WorkoutExercise
from .script import run_migrations
from datetime import datetime, date, timedelta
import requests
import json
import os
import random

test_choices = [
    ["chest", "back"],
    ["shoulders", "biceps", "triceps"],
    ["back", "biceps"],
    ["shoulders", "chest", "triceps"],
    ["legs", "cardio"],
    ["cardio", "core"],
    ["legs", "back"],
    ["cardio"],
    ["core"]
]


my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "config/workout_week_config.json")
print(path)

# class GetExercises(View):
#     def get(self, request):
#         response = requests.get(
#             # 'https://exercisedb.p.rapidapi.com/exercises/bodyPartList',
#             # 'https://exercisedb.p.rapidapi.com/exercises/bodyPart/cardio',
#             'https://exercisedb.p.rapidapi.com/exercises',
#             headers={
#                 'X-RapidAPI-Host': 'exercisedb.p.rapidapi.com',
#                 'X-RapidAPI-Key': '1d73d9f222msh5eb0f148f96868cp109b6bjsne4446eeab19b'
#             },
#         )
#         data = response.json()
#         print("LENGTH: ", len(data))
#         return render(request, 'exercises/exercise_list.html', {'exercise_list': data})

class GetExercises(View):
    def get(self, request):
        exercise_list = Exercise.objects.all()
        print("LENGTH: ", len(exercise_list))
        return render(request, 'exercises/list.html', {'exercise_list': exercise_list})

def run_script(request):
    run_migrations()
    return HttpResponse("Completed")

def generate_workout(request):
    if request.method == "GET":
        print("HERE")

    if request.method == "POST":
        f = open(path)
        # returns JSON object as
        # a dictionary
        data = json.load(f)
        # Gets current weekday
        current_weekday = datetime.today().weekday()
        # Gets previous strength workout date
        previous_strength_workout_date = datetime.today() - timedelta(days=2)
        # Gets previous strength workout muscle target
        print("previous_strength_workout_date: ", previous_strength_workout_date)
        # previous_strength_workout_target = Workout.objects.get(workout_date=previous_strength_workout_date).workout_target.split('-')
        previous_strength_workout_target = ["shoulders", "chest", "triceps"]
        # Choices random muscle target
        choice = random.choice(data[str(current_weekday)])
        # Makes sure the prevous muscle target isn't the same as the current muscle target
        while no_repeat_target_muscle(previous_strength_workout_target, choice['target'], current_weekday):
            choice = random.choice(data[str(current_weekday)])
        workout = get_exercises_for_workout(choice['target'])
        workout_target = "-".join(choice['target'])
        new_workout = Workout.objects.create(workout_target=workout_target)
        for order, exercise in enumerate(workout):
            WorkoutExercise.objects.create(exercise=exercise, workout=new_workout, order=order+1)
        serialized_workout = ExerciseSerializer(workout).all_exercises
        return JsonResponse(data = serialized_workout, status=200)
    return render(request, 'exercises/generate_workout.html', {})

def daily_workout(request):
    if request.method == "GET":
        workout = Workout.objects.filter(workout_date=date.today())[0]
        workout_exercises_object = WorkoutExercise.objects.filter(workout=workout).order_by('order')
        workout_exercises = []
        for exercise in workout_exercises_object:
            print(f"{exercise.order}: {Exercise.objects.get(id=exercise.exercise_id).name}")
            workout_exercises.append(exercise.exercise)
        serialized_workout = ExerciseSerializer(workout_exercises).all_exercises
        return JsonResponse(data = serialized_workout, status=200)


