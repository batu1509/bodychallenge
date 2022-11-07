# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django import forms

# Internal:
from .models import WorkoutTime, WorkoutPlan, Workout
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class DateInput(forms.DateInput):

    input_type = 'date'


class WorkoutTimeForm(forms.ModelForm):

    class Meta:
        model = WorkoutTime
        fields = ('workout_time_name',)


class WorkoutPlanForm(forms.ModelForm):

    class Meta:
        model = WorkoutPlan
        fields = ('first_day',)
        widgets = {'first_day': DateInput(),}


class WorkoutForm(forms.ModelForm):

    class Meta:
        model = Workout
        fields = ('workout_name',)
        labels = {"workout_name": "workout name"}
