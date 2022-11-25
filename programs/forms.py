# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django import forms
from django.core.exceptions import ValidationError
from programs.models import Workout, Exercise, WorkoutExercise, Routine
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class WorkoutForm(forms.ModelForm):
    workout = forms.ModelChoiceField(
        queryset=Workout.objects.all(),
        widget=forms.Select(
            attrs={
                "placeholder": "Exercise",
                "class": "form-select"
            }
        ))
    weekday = forms.ChoiceField(
        choices=Workout.WEEKDAY_CHOICES,
        widget=forms.Select(
            attrs={
                "placeholder": "Weekday",
                "class": "form-select"
            }
        ))
    beginning_time = forms.ChoiceField(
        choices=Workout.HOUR_CHOICES,
        widget=forms.Select(
            attrs={
                "placeholder": "Beginning time",
                "class": "form-select"
            }
        ))
    ending_time = forms.ChoiceField(
        choices=Workout.HOUR_CHOICES,
        widget=forms.Select(
            attrs={
                "placeholder": "Ending time",
                "class": "form-select"
            }
        ))
    exercise = forms.ModelMultipleChoiceField(
        queryset=Exercise.objects.all(),
        widget=forms.SelectMultiple(
            attrs={
                "placeholder": "Exercise",
                "class": "form-select"
            }
        )
    )

    def clean(self):
        if self.cleaned_data["ending_time"] <= self.cleaned_data["beginning_time"]:
            raise ValidationError("Beginning time must be earlier that ending time")
        for exercise in self.cleaned_data["exercise"]:
            if exercise != self.cleaned_data["muscles"]:
                raise ValidationError("The trainer's sport and workout's sport must be the same")
        return super(WorkoutForm, self).clean()

    class Meta:
        model = Workout
        fields = (
            "exercise",
            "weekday",
            "beginning_time",
            "ending_time",
            "muscles"
        )


class WorkoutSearchForm(forms.Form):
    name = forms.CharField(
        max_length=63,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by sport's name",
                   "class": "form-control d-inline w-25"}
        )
    )