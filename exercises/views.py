from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from exercises.serializers import ExerciseSerializer, WorkoutSerializer, UserExerciseSerializer
from .workout_generator import get_exercises_for_workout, no_repeat_target_muscle, previous_workout_two_days_ago, generate_ab_workout
from exercises.models import Exercise, FavoriteWorkout, UserExercise, Workout, WorkoutExercise, DailyWorkout
from exercises.forms.favorite_workout_form import FavoriteWorkoutForm
from django.shortcuts import redirect, get_object_or_404
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
        exercise_list = Exercise.objects.all().order_by('id')
        return render(request, 'exercises/exercise_list.html', {'exercise_list': exercise_list})

def run_script(request):
    if request.method == "POST":
        if request.user.is_authenticated and request.user.is_staff:
            run_migrations(request)
            return HttpResponse("Completed")
        else:
            return HttpResponse("Unauthorized")

    if request.method == "GET":
        if request.user.is_authenticated and request.user.is_staff:
            return render(request, 'staff/write_to_csv.html', {'type': "Migrate CSV"})
        else:
            return HttpResponse("Unauthorized")

def generate_workout(request):
    if request.method == "GET":
        us_east = pytz.timezone("America/New_York")
        east_coast_time = datetime.now(us_east)
        current_weekday = datetime.now(us_east).weekday()
        workouts = Workout.objects.order_by('-workout_date')[:20]
        return render(request, 'exercises/generate_workout.html', {'date_time': east_coast_time, 'last_workout_generate': Workout.objects.all().exclude(workout_target='abs').last(), 'workouts': workouts})

    if request.method == "POST" and request.user.is_authenticated and request.user.is_staff:
        us_east = pytz.timezone("America/New_York")
        east_coast_time = datetime.now(us_east)

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
            return JsonResponse(data = {'response': 'success'}, status=200)
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
            return render(request, 'exercises/generate_workout.html', {'date_time': east_coast_time, 'last_workout_generate': Workout.objects.all().exclude(workout_target='abs').last(), 'workouts': Workout.objects.order_by('-workout_date')[:20]})
    else:
        return redirect('/staff/login')

def get_daily_workout(request):
    us_east = pytz.timezone("America/New_York")
    east_coast_time = datetime.now(us_east)
    try:
        if request.method == "GET":
            workout = Workout.objects.filter(workout_date=east_coast_time).exclude(workout_target='abs')[0]
            # print("WORKOUT: ", workout)
            ab_workout = Workout.objects.filter(workout_target='abs').last()
            workout_exercises_object = WorkoutExercise.objects.filter(workout=workout).order_by('order')
            ab_exercises_object = WorkoutExercise.objects.filter(workout=ab_workout).order_by('order')
            workout_exercises = []
            ab_workout_exercises = []
            for exercise in workout_exercises_object:
                workout_exercises.append(exercise.exercise)
            for ab_exercise in ab_exercises_object:
                ab_workout_exercises.append(ab_exercise.exercise)
            serialized_workout = ExerciseSerializer(workout_exercises, workout, workout.total_rounds, ab_workout_exercises).all_exercises
            # workout_data = WorkoutSerializer(workout)
            # print(workout_data.data)
            return JsonResponse(data = serialized_workout, status=200)
    except Exception as e:
        data = {
            'message': 'There was an error',
            'error': True
        }
        return JsonResponse(data=data, status=500)

@csrf_exempt
def start_workout(request):
    us_east = pytz.timezone("America/New_York")
    east_coast_time = datetime.now(us_east)
    if request.method == 'POST':
        status = json.load(request)
        try:
            daily_workout = DailyWorkout.objects.get(workout_date=date.today(), status=status)
            total_daily_workouts = daily_workout.total_workouts
            daily_workout.total_workouts = total_daily_workouts + 1
            daily_workout.save()
        except:
            DailyWorkout.objects.create(workout_date=date.today(), status=status, total_workouts=1)

        return JsonResponse(data = { 'message': 'success'}, status=200)

def generate_daily_workout_cron():
    cron_logger = os.path.join(my_path, "cron/generate_workout.txt")
    us_east = pytz.timezone("America/New_York")
    current_date_time = datetime.now(us_east)
    current_date = date.today()
    try:
        f = open(path)
        # returns JSON object as
        # a dictionary
        data = json.load(f)
        # Gets current weekday
        current_weekday = current_date.weekday()
        # Gets previous strength workout date
        previous_strength_workout_date = current_date - timedelta(days=2)
        # Gets previous strength workout muscle target
        try:
            existing_workout =  Workout.objects.filter(workout_date=current_date).exclude(workout_target='abs')[0]
            return HttpResponse(f'Workout already exists on this date {current_date}')
        except:
            existing_workout = None

        previous_strength_workout_date = current_date - timedelta(days=2)
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
        for order, exercise in enumerate(workout['exercise_list']):
            WorkoutExercise.objects.create(exercise=exercise, workout=new_workout, order=order+1)
        with open(cron_logger, 'a') as j:
            j.write(f"Success: ${current_date_time}\n")
            j.close()
            return "Success"
    except:
        with open(cron_logger, 'a') as j:
            j.write(f"Failure: ${current_date_time}\n")
            j.close()
            return "Failure"


class MoreWorkouts(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        us_east = pytz.timezone("America/New_York")
        east_coast_time = datetime.now(us_east)
        three_days = datetime.now(us_east) - timedelta(days=3)
        try:
            date = request.query_params.get('date') or None
            workout_type = request.query_params.get('workoutType') or None
            if date and workout_type != 'abs':
                past_workout = get_past_workout(date)
                return past_workout
            if date and workout_type == 'abs':
                past_workout = get_workout(date, workout_type)
                return past_workout
            workouts_query = Workout.objects.filter(workout_date__range=(three_days, east_coast_time)).exclude(workout_target='abs')
            # print(workouts_query)
            past_workouts = []
            favorite_workouts = []
            for workout in workouts_query:
                try:
                    favorites = workout.favorite_workouts.get(user=request.user)
                except FavoriteWorkout.DoesNotExist:
                    favorites = None
                workout_serializer = WorkoutSerializer(workout)
                past_workouts.append(workout_serializer.data)
            return Response(past_workouts, status=200)
        except Exception as e:
            print("EXCEPTION: ", e)
            data = {
                'message': e
            }
            return Response(data, status=500)

def get_workout(date, workout_type):
    try:
        workout = Workout.objects.filter(workout_date=date, workout_target=workout_type)[0]
        workout_exercises_object = WorkoutExercise.objects.filter(workout=workout).order_by('order')
        workout_exercises = []
        ab_workout_exercises = []
        workout_target = workout.workout_target.split('-')
        for exercise in workout_exercises_object:
            workout_exercises.append(exercise.exercise)
        serialized_workout = ExerciseSerializer(workout_exercises, workout, workout.total_rounds, ab_workout_exercises).all_exercises
        return Response(serialized_workout, status=200)
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
        workout_exercises = []
        ab_workout_exercises = []
        workout_target = workout.workout_target.split('-')
        for exercise in workout_exercises_object:
            workout_exercises.append(exercise.exercise)
        for ab_exercise in ab_exercises_object:
            ab_workout_exercises.append(ab_exercise.exercise)
        serialized_workout = ExerciseSerializer(workout_exercises, workout, workout.total_rounds, ab_workout_exercises).all_exercises
        return Response(serialized_workout, status=200)
    except Exception as e:
        print("EXCEPTION: ", e)
        data = {
            'message': e
        }
        return Response(data, status=500)

class Workouts(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, workout_type, format=None):
        try:
            us_east = pytz.timezone("America/New_York")
            east_coast_time = datetime.now(us_east)
            ten_days = datetime.now(us_east) - timedelta(days=30)
            workouts_query = Workout.objects.filter(workout_target=workout_type).order_by('-id')
            # workouts_query = Workout.objects.filter(workout_date__range=(ten_days, east_coast_time), workout_target=workout_type).exclude(workout_target='abs').order_by('-id')
            workout_serializer = WorkoutSerializer(workouts_query, many=True)
            return JsonResponse(workout_serializer.data, safe=False)
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


# --- Favorite Workout

class FavoriteUserWorkout(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, user_id, workout_id, format=None):
        try:
            if does_favorite_workout_exist(user_id, workout_id):
                return Response({'message': 'User has favorited this workout', 'is_favorite': True}, status=200)
            else:
                return Response({'message': 'User has NOT favorited this workout', 'is_favorite': False}, status=200)
        except Exception as e:
            data = {
                'message': e
            }
            return Response(data, status=500)

    def post(self, request, user_id, workout_id, format=None):
        try:
            query = request.query_params.get('query')
            if query == 'favorite':
                favorite_workout = FavoriteWorkout(user=request.user, workout=Workout.objects.get(id=workout_id))
                form = FavoriteWorkoutForm(instance=favorite_workout)
                if form.is_valid:
                    workout = favorite_workout.save()
                    return Response({'message': 'success'}, status=200)
                return Response({'message': 'failed to save favorite workout'}, status=200)

            if query == 'unfavorite':
                favorite_workout = FavoriteWorkout.objects.get(user=request.user, workout=Workout.objects.get(id=workout_id))
                favorite_workout.delete()
                form = FavoriteWorkoutForm(instance=favorite_workout)
                return Response({'message': 'success'}, status=200)

        except Exception as e:
            data = {
                'message': e
            }
            return Response(data, status=200)

def does_favorite_workout_exist(user_id, workout_id):
    favorite_workout = FavoriteWorkout.objects.filter(user=user_id, workout=workout_id)
    return True if len(favorite_workout) == 1 else False

class AllUsersFavoriteWorkout(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, user_id, format=None):
        try:
            favorite_user_workouts = request.user.users_favorite.all()
            favorite_workouts = []
            for fav_workout in favorite_user_workouts:
                workout_serializer = WorkoutSerializer(fav_workout.workout)
                favorite_workouts.append(workout_serializer.data)
            data = {
                'favorite_workouts': favorite_workouts,
                'total_favorite_workouts': len(favorite_workouts),
            }
            return Response(data, status=200)
        except Exception as e:
            data = {
                'message': e
            }
            return Response(data, status=500)

class UserExerciseRecord(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request, workout_id, exercise_id, user_id, format=None):
        try:
            if request.user.is_premium:
                exercise_info = json.load(request)
                workout = Workout.objects.get(id=workout_id)
                exercise = Exercise.objects.get(id=exercise_id)
                user_exercise = UserExercise.objects.create(workout=workout, exercise=exercise, repetitions=exercise_info['reps'], resistance=exercise_info['resistance'], user=request.user)
                return Response({'status': 'Successfully recorded'}, status=200)
        except Exception as e:
            print("EXCEPTION: ", e)
            data = {
                'message': e
            }
            return Response(data, status=500)

    def get(self, request, workout_id, exercise_id, user_id, format=None):
        try:
            if request.user.is_premium:
                exercise = Exercise.objects.get(id=exercise_id)
                user_exercise = exercise.user_exercises_info.filter(user=request.user).last()
                serialized_data = UserExerciseSerializer(user_exercise)
                return Response(serialized_data.data, status=200)
        except Exception as e:
            print("EXCEPTION: ", e)
            data = {
                'message': e
            }
            return Response(data, status=500)

def is_paid_user(user):
    return user.is_premium
