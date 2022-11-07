# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
import profile
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.views import generic
from django.views.generic import ListView, View
from django.forms import formset_factory
from datetime import timedelta
from django.contrib import messages
from django.db import IntegrityError


# Internal
from .models import Exercise, Workout, WorkoutExercise, periodization
from .filters import ExerciseFilter
from programs.forms import DateInput, WorkoutPlanForm, WorkoutForm, WorkoutTimeForm
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


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



# Workout Plan:

class PlannerView(ListView):

    def get(self, request):

        return render(request, 'planner.html')


class ChooseDate(View):

    def get(self, request):

        return render(request, 'choose_date.html', {'workout_plan_form': WorkoutPlanForm()})

    def post(self, request):

        workout_plan_form = WorkoutPlanForm(request.POST)

        if workout_plan_form.is_valid():
            user = request.user
            day = workout_plan_form.cleaned_data.get('day')
            workout_plan = Workout(user=user, day=day,)

            try:
                workout_plan.save()
                request.session['workout_plan.id'] = workout_plan.pk
                return redirect('add_plan')

            except IntegrityError as e:
                messages.error(request, 'You already have a plan starting on this day.')
                return render(request, 'choose_date.html', {'workout_plan_form': WorkoutPlanForm()})

        else:
            workout_plan_form = WorkoutPlanForm()
            context = {'workout_plan_form': workout_plan_form}

        return render(request, 'view_plans.html', context)


class AddPlan(View):

    def get(self, request):

        try:
            workout_plan_id = request.session.get('workout_plan.id')
            workout_plan = Workout.objects.get(pk=workout_plan_id)
            day1 = workout_plan.day
            day2 = day1 + timedelta(days=1)
            day3 = day1 + timedelta(days=2)
            day4 = day1 + timedelta(days=3)
            day5 = day1 + timedelta(days=4)
            day6 = day1 + timedelta(days=5)
            day7 = day1 + timedelta(days=6)

            formset = formset_factory(WorkoutForm, extra=28)

            context = {'day1': day1, 'day2': day2, 'day3': day3, 'day4': day4, 'day5': day5, 'day6': day6, 'day7': day7,
                       'formset': formset, }
            return render(request, 'add_plan.html', context)

        except:
            messages.error(request, 'An error occurred...')
            return redirect('home')

    def post(self, request):

        try:
            workout_plan_id = request.session.get('workout_plan.id')
            workout_plan = WorkoutExercise.objects.get(pk=workout_plan_id)

            day1 = workout_plan.first_day
            week = [day1, day1 + timedelta(days=1), day1 + timedelta(days=2), day1 + timedelta(days=3), 
                day1 + timedelta(days=4), day1 + timedelta(days=5), day1 + timedelta(days=6),]

            schedule_fields = formset_factory(WorkoutForm, extra=28)
            formset = schedule_fields(request.POST)

            if formset.is_valid():
                field = 0
                for form in formset:
                    workout_name = form.cleaned_data.get('workout_name')
                    if workout_name is None:
                        workout_name = ''
                    workout_day = week[field % 7]

                    if field < 14:
                        workout_time = Workout.objects.get(workout_time_name='AM')
                    else:
                        workout_time = Workout.objects.get(workout_time_name='PM')

                    workout = Workout(workout_name=workout_name, workout_time=workout_time,
                        workout_plan=workout_plan, day=workout_day)
                    workout.save()
                    field += 1
                messages.success(request, 'Your plan has been created.')
                return redirect('view_plans')

        except:
            messages.error(request, 'Something went wrong when adding your plan...')
            return redirect('home')


class ViewPlans(generic.ListView):

    model = Workout
    template_name = 'view_plans.html'
    paginate_by = 1

    def get_queryset(self):

        return Workout.objects.filter(user=self.request.user)


class EditPlan(View):

    def get(self, request, **kwargs):

        try:
            workout_plan_id = self.kwargs['workout_plan_id']
            workout_plan = WorkoutExercise.objects.get(pk=workout_plan_id)

            day1 = workout_plan.first_day
            day2 = day1 + timedelta(days=1)
            day3 = day1 + timedelta(days=2)
            day4 = day1 + timedelta(days=3)
            day5 = day1 + timedelta(days=4)
            day6 = day1 + timedelta(days=5)
            day7 = day1 + timedelta(days=6)

            if request.user == workout_plan.user:
                workouts = Workout.objects.filter(workout_plan=workout_plan_id)
                schedule_fields = formset_factory(WorkoutForm, extra=0)
                field_value = []
                for workout in workouts:
                    field_value.append({'workout_name': workout.workout_name})
                formset = schedule_fields(initial=field_value)

                context = {'day1': day1, 'day2': day2, 'day3': day3,
                           'day4': day4, 'day5': day5, 'day6': day6,
                           'day7': day7, 'workout_plan': workout_plan,
                           'formset': formset, }

                return render(request, 'edit_plan.html', context)

            else:
                messages.info(request, "You cannot edit other user's plans.")
                return redirect('planner_page')

        except:
            messages.error(request, 'An error occurred...')
            return redirect('home')

    def post(self, request, **kwargs):

        try:
            workout_plan = WorkoutExercise.objects.get(
                pk=self.kwargs['workout_plan_id'])

            day1 = workout_plan.day
            week = [
                day1,
                day1 + timedelta(days=1),
                day1 + timedelta(days=2),
                day1 + timedelta(days=3),
                day1 + timedelta(days=4),
                day1 + timedelta(days=5),
                day1 + timedelta(days=6),
            ]

            schedule_fields = formset_factory(WorkoutForm, extra=28)
            formset = schedule_fields(request.POST)
            workouts = Workout.objects.filter(workout_plan=workout_plan)

            if formset.is_valid():
                field = 0
                for form in formset:
                    if workouts:
                        workout_name = form.cleaned_data.get('workout_name')
                        workout = workouts[field]
                        workout.workout_name = workout_name
                        workout.save()

                    else:
                        workout_name = form.cleaned_data.get('workout_name')
                        if workout_name is None:
                            workout_name = ''
                        workout_day = week[field % 7]

                        if field < 14:
                            workout_time = Workout.objects.get(workout_time_name='AM')
                        else:
                            workout_time = Workout.objects.get(workout_time_name='PM')

                        workout = Workout(workout_name=workout_name, workout_time=workout_time,
                            workout_plan=workout_plan, day=workout_day)
                        workout.save()
                    field += 1
                messages.success(request, "Your plan has been amended.")
                return redirect('view_plans')
        except:
            messages.error(request, 'An error occurred...')
            return redirect('home')


class DeletePlan(View):

    def post(self, request, **kwargs):

        try:
            record = WorkoutExercise.objects.get(pk=self.kwargs['workout_plan_id'])
            if request.method == "POST":
                record.delete()
                messages.success(request, "Your plan has been deleted.")
                return redirect('view_plans')
        except:
            messages.error(request, 'An error occurred when deleting your plan.')
            return redirect('home')