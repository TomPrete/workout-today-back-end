from .models import Workout, Exercise, WorkoutExercise
import os
import csv
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "exercises.csv")

def run_migrations():

    with open(path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row['name'])
            if row['equipment'] == None:
                    equipment_type = False
            if row['equipment'] == 'True':
                equipment_type = True
            try:
                exercise = Exercise.objects.get(name=row['name'])
                exercise.muscle_target = row['muscle_target']
                exercise.secondary_target = row['secondary_target']
                exercise.muscle_group = row['muscle_group']
                exercise.push_pull = row['push_pull']
                exercise.difficulty_level = 0
                if row['equipment'] == None:
                    exercise.equipment = False
                if row['equipment'] == 'True':
                    exercise.equipment = True
                exercise.resistance_type = row['resistance_type']
                exercise.quantity = row['quantity']
                exercise.demo_src = row['img']
                exercise.save()
            except:
                Exercise.objects.create(
                    name=row['name'],
                    muscle_target=row['muscle_target'],
                    secondary_target=row['secondary_target'],
                    push_pull=row['push_pull'],
                    muscle_group=row['muscle_group'],
                    difficulty_level = 1,
                    equipment = equipment_type,
                    resistance_type = row['resistance_type'],
                    quantity = row['quantity'],
                    demo_src = row['img']
                    )
    print("Executed...")
    return True

def add_source_gif(request):
    all_exercises = Exercise.objects.all()
    for exercise in all_exercises:
        print(exercise)
        exercise.demo_src = 'https://workouttoday.s3.us-east-2.amazonaws.com/standing_bicep_curls_weights.gif'
        exercise.save()
    return 'complete'
