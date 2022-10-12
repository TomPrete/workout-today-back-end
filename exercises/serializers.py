from builtins import object
from rest_framework import serializers

class ExerciseSerializer(object):
    def __init__(self, workout_exercises, workout, rounds, ab_exercises=None):
        self.workout_exercises = workout_exercises
        self.workout = workout
        self.rounds = rounds
        self.ab_exercises = ab_exercises

    @property
    def all_exercises(self):
        output = {
            'exercises': [],
            'workout_target': self.workout,
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
                'diffulty_level': exercise.diffulty_level,
                'equipment': exercise.equipment,
                'resistance_type': exercise.resistance_type,
                'image_url': exercise.demo_src
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
                    'diffulty_level': ab_exercise.diffulty_level,
                    'equipment': ab_exercise.equipment,
                    'resistance_type': ab_exercise.resistance_type,
                    'image_url': exercise.demo_src
                })
        return output


class WorkoutSerializer(serializers.Serializer):
    workout_date = serializers.DateField()
    workout_target = serializers.CharField(max_length=50)
    total_rounds = serializers.IntegerField()
