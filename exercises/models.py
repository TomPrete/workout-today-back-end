from django.db import models

# Create your models here.
class Exercise(models.Model):
    name = models.CharField(max_length=50)
    muscle_target = models.CharField(max_length=20)
    secondary_target = models.CharField(max_length=20, blank=True, null=True)
    push_pull = models.CharField(max_length=20, blank=True, null=True)
    muscle_group = models.CharField(max_length=20, blank=True, null=True)
    diffulty_level = models.IntegerField(default=0, blank=True, null=True)
    equipment = models.BooleanField(blank=True, null=True)
    resistance_type = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.name}"

class Workout(models.Model):
    workout_date = models.DateField()
    workout_target = models.CharField(max_length=50, blank=True, null=True)
    exercises = models.ManyToManyField(
        Exercise,
        through='WorkoutExercise',
        related_name='workout_exercises'
    )


class WorkoutExercise(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    order = models.IntegerField()

class DailyWorkouts(models.Model):
    workout_date = models.DateField()
    total_workouts = models.IntegerField()
