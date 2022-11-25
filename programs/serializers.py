from rest_framework import serializers
from programs.models import Muscle, MuscleGroup, Level, Routine, RoutineGoal, RoutineType, Equipment, Exercise, ExerciseMechanic, ExerciseType, Workout, WorkoutExercise, WorkoutExerciseSet, WorkoutExerciseSetWithReps, Gender, LinearWorkout, CircularWorkout, repType, IntervalWorkoutExerciseSet

# from django.contrib.auth.models import User
from django.utils import timezone


class MuscleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Muscle
        fields = '__all__'

class MuscleGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = MuscleGroup
        fields = '__all__'

class LevelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Level
        fields = '__all__'

class RoutineSerializer(serializers.ModelSerializer):

    class Meta:
        model = Routine
        fields = '__all__'
        
class RoutineGoalSerializer(serializers.ModelSerializer):

    class Meta:
        model = RoutineGoal
        fields = '__all__'

class RoutineTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = RoutineType
        fields = '__all__'

class EquipmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Equipment
        fields = '__all__'

class ExerciseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Exercise
        fields = '__all__'

class ExerciseMechanicSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExerciseMechanic
        fields = '__all__'

class ExerciseTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExerciseType
        fields = '__all__'

class WorkoutSerializer(serializers.ModelSerializer):

    class Meta:
        model = Workout
        fields = '__all__'

class WorkoutExerciseSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkoutExercise
        fields = '__all__'

class WorkoutExerciseSetSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkoutExerciseSet
        fields = '__all__'

class WorkoutExerciseSetWithRepsSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkoutExerciseSetWithReps
        fields = '__all__'

class GenderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Gender
        fields = '__all__'


class LinearWorkoutSerializer(serializers.ModelSerializer):

    class Meta:
        model = LinearWorkout
        fields = '__all__'

class CircularWorkoutSerializer(serializers.ModelSerializer):

    class Meta:
        model = CircularWorkout
        fields = '__all__'

class repTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = repType
        fields = '__all__'

class IntervalWorkoutExerciseSetSerializer(serializers.ModelSerializer):

    class Meta:
        model = IntervalWorkoutExerciseSet
        fields = '__all__'
        