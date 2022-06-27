from builtins import object

class ExerciseSerializer(object):
    def __init__(self, workout_exercises, workout, rounds):
        self.workout_exercises = workout_exercises
        self.workout = workout
        self.rounds = rounds

    @property
    def all_exercises(self):
        output = {
            "exercises": [],
            "workout_target": self.workout,
            "rounds": self.rounds
        }

        for idx, exercise in enumerate(self.workout_exercises):
            output["exercises"].append({
                "order": idx + 1,
                "name": exercise.name,
                "muscle_target": exercise.muscle_target,
                "secondary_target": exercise.secondary_target,
                "push_pull": exercise.push_pull,
                "muscle_group": exercise.muscle_group,
                "diffulty_level": exercise.diffulty_level,
                "equipment": exercise.equipment,
                "resistance_type": exercise.resistance_type
            })
        return output
