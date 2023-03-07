from django.shortcuts import render
from django.views.generic.list import ListView
from exercises.models import User, Exercise, Workout, WorkoutExercise, DailyWorkout, FavoriteWorkout, UserExercise
# Create your views here.

class GetExercisesList(ListView):
    model = Exercise
    template_name = 'exercise_list.html'
    paginate_by = 20

    def get_queryset(self):
        return Exercise.objects.all().order_by('name')

    def get_context_data(self, **kwargs):
        if self.request.user.is_authenticated and self.request.user.is_staff:
            context = super().get_context_data(**kwargs)
            return context
        else:
            return render(self.request, '404.html', {})

def login(request):
    pass
    # return render(request, )
