# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.views import generic
from django.views.generic import ListView, View
from django.forms import formset_factory

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from .models import Exercise, Workout, WorkoutExercise
from .filters import ExerciseFilter
from programs.forms import WorkoutForm, WorkoutSearchForm

def show_all_exercises_page(ListView):

    context = {}

    filtered_exercises = ExerciseFilter(ListView.GET, queryset=Exercise.objects.all())

    context['filtered_exercises'] = filtered_exercises

    paginated_filtered_exercises = Paginator(filtered_exercises.qs, 8)

    page_number = ListView.GET.get('page')
    exercise_page_obj = paginated_filtered_exercises.get_page(page_number)

    context['exercise_page_obj'] = exercise_page_obj
    context['all_exercises'] = Exercise.objects.all()

    return render(ListView, 'exercises_list.html', context)


class SingleExercise(View):

    def get(self, request, exercise_id):
        exercise = Exercise.objects.get(pk=exercise_id)
        return render(request, 'exercise.html', {'exercise': exercise})

class WorkoutListView(LoginRequiredMixin, generic.ListView):
    model = Workout
    paginate_by = 5
    queryset = Workout.objects.select_related("muscles")
    template_name = "workout_list.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        name = self.request.GET.get("name", "")

        context = super(WorkoutListView, self).get_context_data(**kwargs)
        context["search_form"] = WorkoutSearchForm(initial={
            "name": name
        })

        return context

    def get_queryset(self):
        form = WorkoutSearchForm(self.request.GET)

        if form.is_valid():
            return self.queryset.filter(
                exercise__name__icontains=form.cleaned_data["name"]
            )

        return self.queryset


class WorkoutUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Workout
    form_class = WorkoutForm
    success_url = reverse_lazy("workouts")
    template_name = "workout_form.html"


class WorkoutCreateView(LoginRequiredMixin, generic.CreateView):
    model = Workout
    form_class = WorkoutForm
    success_url = reverse_lazy("workouts")
    template_name = "workout_form.html"

class ProgramsView(LoginRequiredMixin, generic.ListView):
    model = Workout
    template_name = "programs.html"

@login_required
def workout_delete(request, pk):
    Workout.objects.filter(id=pk).delete()
    return HttpResponseRedirect(reverse_lazy("workouts"))


@login_required
def toggle_assign_to_workout(request, pk):
    exercise = Exercise.objects.get(id=request.user.id)
    if (
        Workout.objects.get(id=pk) in exercise.workouts.all()
    ):
        exercise.workouts.remove(pk)
    else:
        exercise.workouts.add(pk)
    return HttpResponseRedirect(reverse_lazy("workouts"))

