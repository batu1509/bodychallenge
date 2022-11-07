# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib import admin

# Internal:
from .models import WorkoutTime, WorkoutPlan, Workout
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


@admin.register(WorkoutTime)
class WorkoutTimeAdmin(admin.ModelAdmin):
    """
    Admin class for the WorkoutTime model
    """
    list_display = ('workout_time_name',)


@admin.register(WorkoutPlan)
class WorkoutPlanAdmin(admin.ModelAdmin):
    """
    Admin class for the WorkoutPlan model
    """
    list_display = (
        'user',
        'first_day',
        'id',
        )
    list_filter = ('user', 'first_day',)


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    """
    Admin class for the Workout model
    """
    list_display = (
        'workout_name',
        'workout_time',
        'workout_plan',
        'day',
    )
    list_filter = (
        'workout_plan',
    )
