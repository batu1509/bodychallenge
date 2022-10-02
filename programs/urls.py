from django.urls import path, include
from programs.views import ProfilImageUpdateView, MuscleViewSet, ProfilViewSet, MuscleGroupViewSet, WorkoutViewSet, ExerciseViewSet, LevelViewSet, GenderViewSet, repTypeViewSet, RoutineViewSet, EquipmentViewSet, RoutineGoalViewSet, RoutineTypeViewSet, LinearWorkoutViewSet, periodizationViewSet, CircularWorkoutViewSet, WorkoutExerciseViewSet, ExerciseTypeViewSet, ExerciseMechanicViewSet, WorkoutExerciseSetViewSet, WorkoutExerciseSetWithRepsViewSet, IntervalWorkoutExerciseSetViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'muscle',MuscleViewSet)
router.register(r'profil',ProfilViewSet)
router.register(r'muscleGroup',MuscleGroupViewSet)
router.register(r'workout',WorkoutViewSet)
router.register(r'exercise',ExerciseViewSet)
router.register(r'gender',GenderViewSet)
router.register(r'level',LevelViewSet)
router.register(r'repType',repTypeViewSet)
router.register(r'routine',RoutineViewSet)
router.register(r'routineType',RoutineTypeViewSet)
router.register(r'routineGoal',RoutineGoalViewSet)
router.register(r'equipment',EquipmentViewSet)
router.register(r'linearWorkout',LinearWorkoutViewSet)
router.register(r'periodization',periodizationViewSet)
router.register(r'circularWorkout',CircularWorkoutViewSet)
router.register(r'workoutExercise',WorkoutExerciseViewSet)
router.register(r'exerciseType',ExerciseTypeViewSet)
router.register(r'exerciseMechanic',ExerciseMechanicViewSet)
router.register(r'workoutExerciseSet',WorkoutExerciseSetViewSet)
router.register(r'workoutExerciseSetWithReps',WorkoutExerciseSetWithRepsViewSet)
router.register(r'intervalWorkoutExerciseSet',IntervalWorkoutExerciseSetViewSet)




urlpatterns = [
    path('', include(router.urls)),
    path('profil_image/', ProfilImageUpdateView.as_view(), name='profilimage'),
]

