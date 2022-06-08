from django.urls import path
from django.views.generic import TemplateView
from .views import GetExercises, run_script, generate_workout, daily_workout

urlpatterns = [
    path('today', daily_workout),
    path('exercises', GetExercises.as_view()),
    path('run', run_script),
    path('generate', generate_workout)
]
