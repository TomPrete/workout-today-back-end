from django.urls import path
from django.views.generic import TemplateView
from .views import GetExercises, run_script, generate_workout, get_daily_workout, start_workout

urlpatterns = [
    path('today', get_daily_workout),
    path('exercises', GetExercises.as_view()),
    path('run', run_script),
    path('generate', generate_workout),
    path('start-workout', start_workout)
]
