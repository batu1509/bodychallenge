# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django import forms

# Internal:
from programs.models import Workout, WorkoutExercise, periodization, Routine
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class DateInput(forms.DateInput):

    input_type = 'date'


class WorkoutTimeForm(forms.ModelForm):

    class Meta:
        model = Workout
        fields = ('day',)


class WorkoutPlanForm(forms.ModelForm):

    class Meta:
        model = Workout
        fields = ('day',)
        widgets = {'day': DateInput(),}


class WorkoutForm(forms.ModelForm):

    class Meta:
        model = Workout
        fields = ('name',)
        labels = {"name": "name"}
