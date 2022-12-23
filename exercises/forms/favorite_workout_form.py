from django.forms import ModelForm
from exercises.models import FavoriteWorkout

class FavoriteWorkoutForm(ModelForm):
    class Meta:
        model = FavoriteWorkout
        fields = ['user', 'workout']
