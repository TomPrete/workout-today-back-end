from django.urls import path
from django.views.generic import TemplateView
from .views import GetExercises, run_script, generate_workout, get_daily_workout, start_workout, MoreWorkouts, Login, FavoriteUserWorkout, UserExerciseRecord, Workouts
from .script import add_source_gif


urlpatterns = [
    path('login', Login.as_view()),
    path('today', get_daily_workout),
    path('exercises', GetExercises.as_view()),
    path('run', run_script),
    # path('add-src', add_source_gif),
    path('generate', generate_workout),
    path('start-workout', start_workout),
    path('more-workouts', MoreWorkouts.as_view()),
    path('workouts/<str:workout_type>/', Workouts.as_view()),
    path('user/<int:user_id>/workout/<int:workout_id>', FavoriteUserWorkout.as_view()),
    path('workout/<int:workout_id>/exercise/<int:exercise_id>/user/<int:user_id>', UserExerciseRecord.as_view()),
]
