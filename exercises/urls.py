from django.urls import path
from django.views.generic import TemplateView
from .views import GetExercises, run_script, generate_workout, get_daily_workout, start_workout, MoreWorkouts, Login
from .script import add_source_gif


urlpatterns = [
    path('login', Login.as_view()),
    path('all-workouts', Login.as_view()),
    path('today', get_daily_workout),
    path('exercises', GetExercises.as_view()),
    path('run', run_script),
    # path('add-src', add_source_gif),
    path('generate', generate_workout),
    path('start-workout', start_workout),
    path('more-workouts', MoreWorkouts.as_view()),
]
