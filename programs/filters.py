from django_filters import rest_framework as filters
from programs.models import Exercise
# from django.core.validators import EMPTY_VALUES


class ExerciseFilter(filters.FilterSet):

    name = filters.CharFilter(lookup_expr='icontains', label="Name")

    class Meta:
        model = Exercise
        fields = ['primaryTargetMuscles', 'level', 'type', 'equipment','mechanics']
