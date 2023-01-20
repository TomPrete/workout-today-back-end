from django.shortcuts import render
from django.views import View
from exercises.models import User, Exercise, Workout, WorkoutExercise, DailyWorkout, FavoriteWorkout, UserExercise
# Create your views here.

class GetExercises(View):
    def get(self, request):
        if request.user.is_authenticated and request.user.is_staff:
            exercise_list = Exercise.objects.all().order_by('id')
            return render(request, 'exercise_list.html', {'all_exercises': exercise_list})
        else:
            return render(request, '<div>Not found</div>', {})

    def put(self, request):
        pass

def login(request):
    pass
    # return render(request, )
