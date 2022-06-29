from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from exercises.serializers import ExerciseSerializer
from .workout_generator import get_exercises_for_workout, no_repeat_target_muscle, previous_workout_two_days_ago, stringify_target_workout, generate_ab_workout
from exercises.models import Exercise, Workout, WorkoutExercise, DailyWorkouts
from .script import run_migrations
from datetime import datetime, date, timedelta
import pytz
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
        us_east = pytz.timezone("America/New_York")
        east_coast_time = datetime.now(us_east)
        current_weekday = datetime.now(us_east).weekday()
        print(current_weekday)
        return render(request, 'exercises/generate_workout.html', {'date_time': east_coast_time, 'last_workout_generate': Workout.objects.last()})

    if request.method == "POST":
        f = open(path)
        # returns JSON object as
        # a dictionary
        data = json.load(f)
        date_response = request.POST['date']
        split_date = date_response.split('-')
        current_date = date(int(split_date[0]),int(split_date[1]),int(split_date[2]))
        current_weekday = current_date.weekday()

        if request.POST.get('abs'):
            print(request.POST['abs'])
            ab_exercises = generate_ab_workout()
            ab_workout = Workout.objects.create(workout_target=request.POST['abs'], workout_date=current_date, total_rounds=1)
            print(ab_workout)
            for order, exercise in enumerate(ab_exercises):
                WorkoutExercise.objects.create(exercise=exercise, workout=ab_workout, order=order+1)
            serialized_workout = ExerciseSerializer(ab_exercises, request.POST['abs'], 1).all_exercises
            return JsonResponse(data = serialized_workout, status=200)
        else:
            previous_strength_workout_date = current_date - timedelta(days=2)
            print("previous_strength_workout_date: ", previous_strength_workout_date)
            try:
                previous_strength_workout_target = Workout.objects.filter(workout_date=previous_strength_workout_date).exclude(workout_target='abs')[0].workout_target.split('-')
            except:
                previous_strength_workout_target = random.choice(data[str(previous_workout_two_days_ago(current_weekday, 2))])['target']
            # Choices random muscle target
            choice = random.choice(data[str(current_weekday)])
            # Makes sure the prevous muscle target isn't the same as the current muscle target
            while no_repeat_target_muscle(previous_strength_workout_target, choice['target'], current_weekday):
                choice = random.choice(data[str(current_weekday)])
            workout = get_exercises_for_workout(choice['target'])
            workout_target = "-".join(choice['target'])
            new_workout = Workout.objects.create(workout_target=workout_target, workout_date=current_date, total_rounds=workout['rounds'])
            print(new_workout)
            for order, exercise in enumerate(workout['exercise_list']):
                WorkoutExercise.objects.create(exercise=exercise, workout=new_workout, order=order+1)
            serialized_workout = ExerciseSerializer(workout['exercise_list'], stringify_target_workout(choice['target']), workout['rounds']).all_exercises
            return JsonResponse(data = serialized_workout, status=200)

def get_daily_workout(request):
    us_east = pytz.timezone("America/New_York")
    east_coast_time = datetime.now(us_east)
    try:
        if request.method == "GET":
            workout = Workout.objects.filter(workout_date=east_coast_time).exclude(workout_target='abs')[0]
            ab_workout = Workout.objects.filter(workout_target='abs').last()
            workout_exercises_object = WorkoutExercise.objects.filter(workout=workout).order_by('order')
            ab_exercises_object = WorkoutExercise.objects.filter(workout=ab_workout).order_by('order')
            workout_exercises = []
            ab_workout_exercises = []
            workout_target = workout.workout_target.split('-')
            for exercise in workout_exercises_object:
                print(f"{exercise.order}: {Exercise.objects.get(id=exercise.exercise_id).name}")
                workout_exercises.append(exercise.exercise)
            for ab_exercise in ab_exercises_object:
                print(f"{exercise.order}: {Exercise.objects.get(id=exercise.exercise_id).name}")
                ab_workout_exercises.append(ab_exercise.exercise)
            serialized_workout = ExerciseSerializer(workout_exercises, stringify_target_workout(workout_target), workout.total_rounds, ab_workout_exercises).all_exercises
            print(serialized_workout)
            return JsonResponse(data = serialized_workout, status=200)
    except:
        print("ERROR")
        return JsonResponse(data = {'error': 'There was an error.'}, status=200)

@csrf_exempt
def start_workout(request):
    us_east = pytz.timezone("America/New_York")
    east_coast_time = datetime.now(us_east)
    if request.method == 'POST':
        status = json.load(request)
        print(status)
        try:
            daily_workout = DailyWorkouts.objects.get(workout_date=date.today(), status=status)
            print(daily_workout)
            total_daily_workouts = daily_workout.total_workouts
            print(total_daily_workouts)
            daily_workout.total_workouts = total_daily_workouts + 1
            daily_workout.save()
        except:
            DailyWorkouts.objects.create(workout_date=date.today(), status=status, total_workouts=1)

        return JsonResponse(data = { 'message': 'success'}, status=200)

def generate_daily_workout_cron():
    cron_logger = os.path.join(my_path, "cron/generate_workout.txt")
    us_east = pytz.timezone("America/New_York")
    east_coast_time = datetime.now(us_east)
    try:
        f = open(path)
        # returns JSON object as
        # a dictionary
        data = json.load(f)
        # Gets current weekday
        current_weekday = east_coast_time.weekday()
        # Gets previous strength workout date
        previous_strength_workout_date = east_coast_time - timedelta(days=2)
        # Gets previous strength workout muscle target
        try:
            previous_strength_workout_target = Workout.objects.get(workout_date=previous_strength_workout_date).exclude(workout_target='abs').workout_target.split('-')
            print(previous_strength_workout_target)
        except:
            previous_strength_workout_target = random.choice(data[str(previous_workout_two_days_ago(current_weekday, 2))])['target']
        # Choices random muscle target
        choice = random.choice(data[str(current_weekday)])
        # Makes sure the prevous muscle target isn't the same as the current muscle target
        while no_repeat_target_muscle(previous_strength_workout_target, choice['target'], current_weekday):
            choice = random.choice(data[str(current_weekday)])
        workout = get_exercises_for_workout(choice['target'])
        workout_target = "-".join(choice['target'])
        new_workout = Workout.objects.create(workout_target=workout_target, workout_date=east_coast_time)
        print(new_workout)
        for order, exercise in enumerate(workout):
            WorkoutExercise.objects.create(exercise=exercise, workout=new_workout, order=order+1)
        with open(cron_logger, 'a') as j:
            j.write(f"Success: ${east_coast_time}\n")
            j.close()
            return "Success"
    except:
        with open(cron_logger, 'a') as j:
            j.write(f"Failure: ${east_coast_time}\n")
            j.close()
            return "Failure"


