from django.db import models
from PIL import Image
from django.contrib.auth.models import User
# Create your models here.


class MuscleGroup(models.Model):

    name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name

class Muscle(models.Model):

    name = models.CharField(max_length=255, null=True )
    group = models.ForeignKey(MuscleGroup, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

class Level(models.Model):

    level = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.level

class RoutineGoal(models.Model):

    goal = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.goal

class RoutineType(models.Model):

    type = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.type

class Equipment(models.Model):

    name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name

class ExerciseType(models.Model):

    type = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.type

class ExerciseMechanic(models.Model):

    mechanic = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.mechanic

class Exercise(models.Model):

    name = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=255, null=True)
    image = models.ImageField(null=True, blank=True, upload_to = 'exercise_photos/%Y/%m/')
    video = models.CharField(max_length=255, null=True)
    primaryTargetMuscles = models.ManyToManyField(Muscle, blank=False, related_name='primaryTargetMuscles')
    secondaryTargetMuscles = models.ManyToManyField(Muscle, blank=False, related_name='secondaryTargetMuscles')
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, null=True)
    level = models.ForeignKey(Level, on_delete=models.CASCADE, null=True)
    type = models.ForeignKey(ExerciseType, on_delete=models.CASCADE, null=True)
    mechanics = models.ForeignKey(ExerciseMechanic, on_delete=models.CASCADE, null=True)
    intervalOnly = models.BooleanField(null=True)

    def __str__(self):
        return self.name


class Gender(models.Model):

    name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name

class Routine(models.Model):
    
    name = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=255, null=True)
    level = models.ManyToManyField(Level, blank=False, related_name='lev')
    goal = models.ForeignKey(RoutineGoal, on_delete=models.CASCADE, null=True)
    type = models.ForeignKey(RoutineType, on_delete=models.CASCADE, null=True)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, null=True)
    image = models.ImageField(null=True, blank=True)
    createDate = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.name  

class periodization(models.Model):

    name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name

class Workout(models.Model):

    name = models.CharField(max_length=255, null=True)
    day = models.IntegerField(null=True)
    periodization = models.ForeignKey(periodization, on_delete=models.CASCADE, null=True)
    routineld = models.ForeignKey(Routine, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

class LinearWorkout(models.Model):

    workoutId = models.ForeignKey(Workout, on_delete=models.CASCADE, null=True)

class CircularWorkout(models.Model):

    workoutId = models.ForeignKey(Workout, on_delete=models.CASCADE, null=True)
    lapCount = models.IntegerField(null=True)
    restBetweenLaps = models.IntegerField(null=True)

class WorkoutExercise(models.Model):

    # id =  models.AutoField(primary_key=True)
    workoutId = models.ForeignKey(Workout, on_delete=models.CASCADE, null=True)
    workoutTypeId = models.ForeignKey(LinearWorkout, on_delete=models.CASCADE, null=True)
    exerciseId = models.ForeignKey(Exercise, on_delete=models.CASCADE, null=True)
    restTime = models.IntegerField(null=True, blank=True)
    linkedExercise = models.IntegerField(null=True)

class WorkoutExerciseSet(models.Model):

    workoutExerciseİd = models.ForeignKey(WorkoutExercise, on_delete=models.CASCADE, null=True)

class repType(models.Model):

    name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name

class WorkoutExerciseSetWithReps(models.Model):

    workoutExerciseSetId = models.ForeignKey(WorkoutExerciseSet, on_delete=models.CASCADE, null=True)
    repCount = models.IntegerField(null=True)
    repType = models.ForeignKey(repType, on_delete=models.CASCADE, null=True)

class IntervalWorkoutExerciseSet(models.Model):

    workoutExerciseSetId = models.ForeignKey(WorkoutExerciseSet, on_delete=models.CASCADE, null=True)
    duration = models.IntegerField(null=True)



