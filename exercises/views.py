from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from exercises.serializers import ExerciseSerializer, WorkoutSerializer
from .workout_generator import get_exercises_for_workout, no_repeat_target_muscle, previous_workout_two_days_ago, stringify_target_workout, generate_ab_workout
from exercises.models import Exercise, Workout, WorkoutExercise, DailyWorkouts
from django.shortcuts import redirect
from .script import run_migrations
from workout_today.views import page_not_found_view
from datetime import datetime, date, timedelta
from rest_framework.views import APIView
from rest_framework import authentication, permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from django.contrib.auth.views import LoginView
import pytz
import requests
import json
import os
import random
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "config/workout_week_config.json")


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

class GetExercises(View):
    def get(self, request):
        exercise_list = Exercise.objects.all()
        return render(request, 'exercises/list.html', {'exercise_list': exercise_list})

def run_script(request):
    run_migrations()
    return HttpResponse("Completed")

def generate_workout(request):
    print("USER: ", request.user.is_authenticated)
    print("USER: ", request.user)
    print("USER: ", request.user.is_staff)
    if request.method == "GET":
        us_east = pytz.timezone("America/New_York")
        east_coast_time = datetime.now(us_east)
        current_weekday = datetime.now(us_east).weekday()
        workouts = Workout.objects.order_by('-workout_date')[:20]
        return render(request, 'exercises/generate_workout.html', {'date_time': east_coast_time, 'last_workout_generate': Workout.objects.all().exclude(workout_target='abs').last(), 'workouts': workouts})

    if request.method == "POST" and request.user.is_authenticated and request.user.is_staff:
        f = open(path)
        # returns JSON object as
        # a dictionary
        data = json.load(f)
        date_response = request.POST['date']

        split_date = date_response.split('-')
        current_date = date(int(split_date[0]),int(split_date[1]),int(split_date[2]))
        current_weekday = current_date.weekday()

        if request.POST.get('abs'):
            ab_exercises = generate_ab_workout()
            ab_workout = Workout.objects.create(workout_target=request.POST['abs'], workout_date=current_date, total_rounds=1)
            print(ab_workout)
            for order, exercise in enumerate(ab_exercises):
                WorkoutExercise.objects.create(exercise=exercise, workout=ab_workout, order=order+1)
            serialized_workout = ExerciseSerializer(ab_exercises, request.POST['abs'], 1).all_exercises
            return JsonResponse(data = serialized_workout, status=200)
        else:
            try:
                existing_workout =  Workout.objects.filter(workout_date=date_response).exclude(workout_target='abs')[0]
                return HttpResponse(f'Workout already exists on this date {date_response}')
            except:
                existing_workout = None

            previous_strength_workout_date = current_date - timedelta(days=2)
            # print("previous_strength_workout_date: ", previous_strength_workout_date)
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
            # print(new_workout)
            for order, exercise in enumerate(workout['exercise_list']):
                WorkoutExercise.objects.create(exercise=exercise, workout=new_workout, order=order+1)
            serialized_workout = ExerciseSerializer(workout['exercise_list'], stringify_target_workout(choice['target']), workout['rounds']).all_exercises
            return JsonResponse(data = serialized_workout, status=200)
    else:
        return redirect('/staff/login')

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
                workout_exercises.append(exercise.exercise)
            for ab_exercise in ab_exercises_object:
                ab_workout_exercises.append(ab_exercise.exercise)
            serialized_workout = ExerciseSerializer(workout_exercises, stringify_target_workout(workout_target), workout.total_rounds, ab_workout_exercises).all_exercises
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
        try:
            daily_workout = DailyWorkouts.objects.get(workout_date=date.today(), status=status)
            total_daily_workouts = daily_workout.total_workouts
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
            # print(previous_strength_workout_target)
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

class MoreWorkouts(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        us_east = pytz.timezone("America/New_York")
        east_coast_time = datetime.now(us_east)
        one_day = datetime.now(us_east) - timedelta(days=1)
        two_days = datetime.now(us_east) - timedelta(days=2)
        three_days = datetime.now(us_east) - timedelta(days=3)
        try:
            date = request.query_params.get('date') or None
            if date:
                past_workout = get_past_workout(date)
                return past_workout
            workouts_query = Workout.objects.filter(workout_date__range=(three_days, east_coast_time)).exclude(workout_target='abs')
            past_workouts = []
            for workout in workouts_query:
                workout_serializer = WorkoutSerializer(workout)
                past_workouts.append(workout_serializer.data)
            print(past_workouts)
            return Response(past_workouts, status=200)
        except Exception as e:
            print("EXCEPTION: ", e)
            data = {
                'message': e
            }
            return Response(data, status=500)

def get_past_workout(date):
    try:
        workout = Workout.objects.filter(workout_date=date).exclude(workout_target='abs')[0]
        ab_workout = Workout.objects.filter(workout_target='abs').last()
        workout_exercises_object = WorkoutExercise.objects.filter(workout=workout).order_by('order')
        ab_exercises_object = WorkoutExercise.objects.filter(workout=ab_workout).order_by('order')
        print(workout_exercises_object)
        workout_exercises = []
        ab_workout_exercises = []
        workout_target = workout.workout_target.split('-')
        for exercise in workout_exercises_object:
            workout_exercises.append(exercise.exercise)
        for ab_exercise in ab_exercises_object:
            ab_workout_exercises.append(ab_exercise.exercise)
        serialized_workout = ExerciseSerializer(workout_exercises, stringify_target_workout(workout_target), workout.total_rounds, ab_workout_exercises).all_exercises
        return Response(serialized_workout, status=200)
    except Exception as e:
        print("EXCEPTION: ", e)
        data = {
            'message': e
        }
        return Response(data, status=500)

# ------ STAFF SITE
class Login(LoginView):
    next_page='/api/generate'
    redirect_authenticated_user=True
