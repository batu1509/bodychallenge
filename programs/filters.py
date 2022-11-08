from cProfile import label
from dataclasses import field, fields
from django_filters import rest_framework as filters
from django_filters import ModelChoiceFilter
from programs.models import Exercise


class ExerciseFilter(filters.FilterSet):

    name = filters.CharFilter(lookup_expr='icontains', label="Exercise Name")


    class Meta:
        model = Exercise
        fields = ['primaryTargetMuscles', 'level', 'type', 'equipment','mechanics',]
                


