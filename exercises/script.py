from .models import Workout, Exercise, WorkoutExercise
import os
import csv
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "exercises.csv")

def run_migrations():

    with open(path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row)
            try:
                exercise = Exercise.objects.get(name=row['name'])
            except:
                Exercise.objects.create(name=row['name'], muscle_target=row['muscle_target'],secondary_target=row['secondary_target'],push_pull=row['push_pull'],muscle_group=row['muscle_group'])
    print("Executed...")
    return True

