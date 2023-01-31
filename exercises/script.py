from django.shortcuts import render
from django.conf import settings
from .models import Workout, Exercise, WorkoutExercise
from django.http import HttpResponse
import os
import csv
my_path = os.path.abspath(os.path.dirname(__file__))

def run_migrations(request):
    csv_type = request.POST.get('csv-type')
    csv_path = os.path.join(my_path, f"exercises_{csv_type}.csv")
    with open(csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # if row['equipment'] == 'FALSE':
            #     print(False)
            #     equipment_type = False
            # if row['equipment'] == 'TRUE':
            #     print(True)
            #     equipment_type = True
            try:
                exercise = Exercise.objects.get(id=row['id'])
                print(exercise)
                exercise.muscle_target = row['muscle_target']
                exercise.secondary_target = row['secondary_target']
                exercise.muscle_group = row['muscle_group']
                exercise.push_pull = row['push_pull']
                exercise.difficulty_level = 0
                if row['equipment'] != 'TRUE':
                    exercise.equipment = False
                if row['equipment'] == 'TRUE':
                    exercise.equipment = True
                exercise.resistance_type = row['resistance_type']
                exercise.quantity = row['quantity']
                exercise.demo_src = row['demo_src']
                exercise.save()
            except:
                print("HERE")
                return HttpResponse(f"There was an error with Exercise: {exercise.id}")
    print("Executed...")
    return True

def add_source_gif(request):
    all_exercises = Exercise.objects.all()
    for exercise in all_exercises:
        print(exercise)
        exercise.demo_src = 'https://workouttoday.s3.us-east-2.amazonaws.com/standing_bicep_curls_weights.gif'
        exercise.save()
    return 'complete'


def write_exercises_to_csv(request):
    csv_type = request.POST.get('csv-type')
    if request.method == 'POST' and request.user.is_authenticated and request.user.is_staff:
        csv_path = os.path.join(my_path, f"exercises_{csv_type}.csv")
        all_exercises_query = Exercise.objects.all()
        all_exercises = []
        for exercise in all_exercises_query:
            individual_exercise = {
                "id": exercise.id,
                "name": exercise.name,
                "muscle_target": exercise.muscle_target,
                "secondary_target": exercise.secondary_target,
                "push_pull": exercise.push_pull,
                "muscle_group": exercise.muscle_group,
                "difficulty_level": exercise.difficulty_level,
                "equipment": exercise.equipment,
                "resistance_type": exercise.resistance_type,
                "demo_src": exercise.demo_src,
                "quantity": exercise.quantity
            }
            all_exercises.append(individual_exercise)
        write_to_csv(all_exercises, csv_path)
        return HttpResponse("Done")

    if request.method == "GET":
        return render(request, 'staff/write_to_csv.html', {'type': "Write"})

def download_exercise_csv(request):
    if request.method == 'POST' and request.user.is_authenticated and request.user.is_staff:
        file_path = os.path.join(settings.MEDIA_ROOT, path)
        print("FILE PATH: ", file_path)
        if os.path.exists(file_path):
            with open(file_path, 'rb') as fh:
                response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
                response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
                return response
            raise Http404

    if request.method == "GET":
        return render(request, 'staff/write_to_csv.html', {'type': "Download"})

def write_to_csv(exercise_arr, path):
    with open(path, 'w') as file:
        exercise_csv = csv.writer(file)
        exercise_csv.writerow(['id','name','muscle_target','secondary_target','push_pull','muscle_group','diffulty_level','equipment','resistance_type','demo_src','quantity'])
        for exercise in exercise_arr:
            exercise_csv.writerow([exercise['id'],exercise['name'],exercise['muscle_target'],exercise['secondary_target'],exercise['push_pull'],exercise['muscle_group'],exercise['difficulty_level'],exercise['equipment'],exercise['resistance_type'],exercise['demo_src'],exercise['quantity']])
    return True
