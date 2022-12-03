from builtins import object
from rest_framework import serializers
from .workout_generator import stringify_target_workout
from .models import Exercise, WorkoutExercise, Workout, UserExercise

class ExerciseSerializer(object):
    def __init__(self, workout_exercises, workout, rounds, ab_exercises=None):
        self.workout_exercises = workout_exercises
        self.workout = workout
        self.rounds = rounds
        self.ab_exercises = ab_exercises

    @property
    def all_exercises(self):
        output = {
            'workout_id': self.workout.id,
            'exercises': [],
            'workout_target': stringify_target_workout(self.workout.workout_target.split('-')),
            'rounds': self.rounds,
            'ab_exercises': [],
        }

        for idx, exercise in enumerate(self.workout_exercises):
            output['exercises'].append({
                'order': idx + 1,
                'name': exercise.name,
                'muscle_target': exercise.muscle_target,
                'secondary_target': exercise.secondary_target,
                'push_pull': exercise.push_pull,
                'muscle_group': exercise.muscle_group,
                'difficulty_level': exercise.difficulty_level,
                'equipment': exercise.equipment,
                'resistance_type': exercise.resistance_type,
                'image_url': exercise.demo_src,
                'id': exercise.id,
                'quantity': exercise.quantity
            })
        if self.ab_exercises:
            for idx, ab_exercise in enumerate(self.ab_exercises):
                output['ab_exercises'].append({
                    'order': idx + 1,
                    'name': ab_exercise.name,
                    'muscle_target': ab_exercise.muscle_target,
                    'secondary_target': ab_exercise.secondary_target,
                    'push_pull': ab_exercise.push_pull,
                    'muscle_group': ab_exercise.muscle_group,
                    'difficulty_level': ab_exercise.difficulty_level,
                    'equipment': ab_exercise.equipment,
                    'resistance_type': ab_exercise.resistance_type,
                    'image_url': ab_exercise.demo_src,
                    'id': ab_exercise.id,
                    'quantity': ab_exercise.quantity
                })
        return output
# class ExerciseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Exercise
#         fields = ['id', 'name', 'muscle_target', 'secondary_target', 'push_pull', 'muscle_group', 'equipment', 'resistance_type', 'demo_src']

# class WorkoutExerciseSerializer(serializers.ModelSerializer):
#     exercise = ExerciseSerializer(many=True, read_only=True)
#     class Meta:
#         model = WorkoutExercise
#         fields = ['id', 'order', 'exercise']


class WorkoutSerializer(serializers.ModelSerializer):
    # exercises = ExerciseSerializer(many=True, read_only=True)
    class Meta:
        model = Workout
        fields = ['id', 'total_rounds', 'workout_target', 'workout_date']

class UserExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserExercise
        fields = ['id', 'repetitions', 'resistance', 'exercise']
