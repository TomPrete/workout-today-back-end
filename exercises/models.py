from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator

class User(AbstractUser):
    is_premium = models.BooleanField(null=True, blank=True, default=False)
class Exercise(models.Model):
    name = models.CharField(max_length=50)
    muscle_target = models.CharField(max_length=20)
    secondary_target = models.CharField(max_length=20, blank=True, null=True)
    push_pull = models.CharField(max_length=20, blank=True, null=True)
    muscle_group = models.CharField(max_length=20, blank=True, null=True)
    difficulty_level = models.IntegerField(default=0, blank=True, null=True)
    equipment = models.BooleanField(blank=True, null=True)
    resistance_type = models.CharField(max_length=50, blank=True, null=True)
    demo_src = models.CharField(max_length=255, blank=True, null=True)
    quantity = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return f"{self.name}"

class Workout(models.Model):
    workout_date = models.DateField()
    workout_target = models.CharField(max_length=50, blank=True, null=True)
    total_rounds = models.IntegerField(blank=True, null=True)
    exercises = models.ManyToManyField(
        Exercise,
        through='WorkoutExercise',
        related_name='workout_exercises'
    )

    def __str__(self):
        return f"{self.workout_date}: {self.workout_target}"
class WorkoutExercise(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    order = models.IntegerField()

    def __str__(self):
        return f"{self.workout.workout_target} - {self.workout.workout_date}: {self.exercise.name} ({self.order})"

class DailyWorkouts(models.Model):
    workout_date = models.DateField()
    total_workouts = models.IntegerField()
    status = models.CharField(max_length=8)

class FavoriteWorkouts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name='favorite_workouts')

    def __str__(self):
        return f"{self.workout}"

class UserExercise(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name='user_exercises_info')
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users_exercises')
    repetitions = models.IntegerField(validators=[MinValueValidator(0)], blank=True, null=True)
    resistance = models.CharField(max_length=20, blank=True, null=True, default='')

