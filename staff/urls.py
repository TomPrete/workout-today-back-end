from django.urls import path
from django.views.generic import TemplateView
from .views import GetExercisesList
from exercises.views import Login


urlpatterns = [
    path('exercise-list', GetExercisesList.as_view(), name='exercise-list'),
    path('login/', Login.as_view(), name='login'),
]
