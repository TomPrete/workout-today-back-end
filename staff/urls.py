from django.urls import path
from django.views.generic import TemplateView
from .views import GetExercises


urlpatterns = [
    path('exercise-list/', GetExercises.as_view(), name='exercise-list'),
]
