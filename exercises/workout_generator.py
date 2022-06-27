from .models import Exercise
from django.db.models import Q
import random
import math

def get_exercises_for_workout(workout_choices):
    try:
        workout_set_quantity_options = ['single', 'double', 'triple']
        workout_set_quantity = random.choice(workout_set_quantity_options)
        print("ROUNDS: ", workout_set_quantity)
        if workout_set_quantity == 'single':
            exercise_list = get_exercises(workout_choices, 20)
            return {'exercise_list': [*exercise_list], 'rounds': 1}
        elif workout_set_quantity == 'double':
            exercise_list = get_exercises(workout_choices, 10)
            return {'exercise_list': [*exercise_list, *exercise_list], 'rounds': 2}
        else:
            exercise_list = get_exercises(workout_choices, 7)
            return {'exercise_list': [*exercise_list, *exercise_list, *exercise_list], 'rounds': 3}

    except:
        return "there was an error"

def get_exercises(workout_choices, number):
    unordered_exercises = []
    for choice in workout_choices:
        unordered_exercises.append(Exercise.objects.filter(muscle_target=choice).order_by("?")[:(math.ceil(number/len(workout_choices)))])
    return sort_exercises_by_target(unordered_exercises, workout_choices)

def sort_exercises_by_target(unordered_exercises, workout_choices):
    ordered_exercises = []
    max_num_exercises = number_of_target_group_exercises(unordered_exercises)
    workout_choices_length = len(workout_choices)
    if workout_choices_length == 1:
        return unordered_exercises[0]
    for idx in range(max_num_exercises):
        if len(unordered_exercises[0]) > idx:
            ordered_exercises.append(unordered_exercises[0][idx])
        if len(unordered_exercises[1]) > idx:
            ordered_exercises.append(unordered_exercises[1][idx])
        if workout_choices_length == 3:
            if len(unordered_exercises[2]) > idx:
                ordered_exercises.append(unordered_exercises[2][idx])
    print_target_group(ordered_exercises)
    return ordered_exercises

def iterate_choice_idx(workout_choices, current_choice_idx):
    if current_choice_idx == len(workout_choices)-1:
        return 0
    return current_choice_idx + 1

def number_of_target_group_exercises(unordered_exercises):
    max_num_exercises = 0
    for exercise_group in unordered_exercises:
        max_num_exercises = len(exercise_group) if len(exercise_group) > max_num_exercises else len(exercise_group)
    return max_num_exercises

def print_target_group(workout):
    for exercise in workout:
        print(exercise.muscle_target)

# Returns Boolean if a current target muscle was targeted in the previous strength workout
def no_repeat_target_muscle(prevoius_target, current_target, current_weekday):
    repeated_target = [target for target in current_target if target in prevoius_target]
    if len(repeated_target) and current_weekday in [0,2,4]:
        return True
    return False

def previous_workout_two_days_ago(current_day, days_before_today):
    previous_day = current_day - days_before_today
    if previous_day < 0:
        previous_day = 7 + previous_day
    return previous_day

def stringify_target_workout(workout_target_arr):
    if len(workout_target_arr) == 1:
        return workout_target_arr[0].capitalize()
    elif (len(workout_target_arr) == 2):
        return f"{workout_target_arr[0].capitalize()} & {workout_target_arr[1].capitalize()}"
    else:
        return f"{workout_target_arr[0].capitalize()}, {workout_target_arr[1].capitalize()} & {workout_target_arr[2].capitalize()}"

