from django.contrib import admin
from users.models import Profile, ActivityLevel, BodyWeight, BodyHeight, BodyVitalsLog, MeasurementParameter, MeasurementUnit, SavedRoutine
from programs.models import Muscle, MuscleGroup, Level, Routine, RoutineGoal, RoutineType, Equipment, Exercise, ExerciseMechanic, ExerciseType, Workout, WorkoutExercise, WorkoutExerciseSet, WorkoutExerciseSetWithReps, Gender, periodization, LinearWorkout, CircularWorkout, repType, IntervalWorkoutExerciseSet

# Register your models here.
# class RoutineAdmin(admin.ModelAdmin):
#     list_display = ("name","description")
#     list_editable = ("",)
#     search_fields = ("",)
#     readonly_fields = ("",)
#     list_filter = ("",)

admin.site.register(Profile)
admin.site.register(ActivityLevel)
admin.site.register(BodyWeight)
admin.site.register(BodyHeight)
admin.site.register(SavedRoutine)
admin.site.register(MeasurementUnit)
admin.site.register(MeasurementParameter)
admin.site.register(BodyVitalsLog)

admin.site.register(Muscle)
admin.site.register(MuscleGroup)
admin.site.register(Level)
admin.site.register(Routine)
admin.site.register(RoutineGoal)
admin.site.register(RoutineType)
admin.site.register(Equipment)
admin.site.register(Exercise)
admin.site.register(ExerciseMechanic)
admin.site.register(ExerciseType)
admin.site.register(Workout)
admin.site.register(WorkoutExercise)
admin.site.register(WorkoutExerciseSet)
admin.site.register(WorkoutExerciseSetWithReps)
admin.site.register(Gender)
admin.site.register(periodization)
admin.site.register(LinearWorkout)
admin.site.register(CircularWorkout)
admin.site.register(repType)
admin.site.register(IntervalWorkoutExerciseSet)


