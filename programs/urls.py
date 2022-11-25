from django.urls import path, include
from programs.viewset import ProfilImageUpdateView, MeasurementUnitViewSet, MeasurementParameterViewSet, SavedRoutineViewSet, BodyVitalsLogViewSet, ActivityLevelViewSet, MuscleViewSet, ProfilViewSet, MuscleGroupViewSet, WorkoutViewSet, ExerciseViewSet, LevelViewSet, GenderViewSet, repTypeViewSet, RoutineViewSet, EquipmentViewSet, RoutineGoalViewSet, RoutineTypeViewSet, LinearWorkoutViewSet, CircularWorkoutViewSet, WorkoutExerciseViewSet, ExerciseTypeViewSet, ExerciseMechanicViewSet, WorkoutExerciseSetViewSet, WorkoutExerciseSetWithRepsViewSet, IntervalWorkoutExerciseSetViewSet
from rest_framework.routers import DefaultRouter
from programs import views

router = DefaultRouter()
router.register(r'muscle',MuscleViewSet)
router.register(r'profil',ProfilViewSet)
router.register(r'activityLevel',ActivityLevelViewSet)
router.register(r'measurementUnit',MeasurementUnitViewSet)
router.register(r'measurementParameter',MeasurementParameterViewSet)
router.register(r'savedRoutine',SavedRoutineViewSet)
router.register(r'bodyVitalsLog',BodyVitalsLogViewSet)
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
    path('exercises', views.show_all_exercises_page, name='exercises'),
    path('show_exercise/<exercise_id>', views.SingleExercise.as_view(), name='show_exercise'),
    path("workouts/", views.WorkoutListView.as_view(), name="workout-list"),
    path("workouts/<int:pk>/toggle-assign/", views.toggle_assign_to_workout, name="toggle-workout-assign"),
    path("workouts/<int:pk>/update", views.WorkoutUpdateView.as_view(), name="workout-update"),
    path("workouts/create", views.WorkoutCreateView.as_view(), name="workout-create"),
    path("workouts/<int:pk>/delete", views.workout_delete, name="workout-delete"),
    path("workouts/<int:pk>/programs", views.ProgramsView.as_view(), name="workout-programs"),
]


# urlpatterns = [
#     path('planner', views.PlannerView.as_view(), name='planner_page'),
#     path('choose_date/', views.ChooseDate.as_view(), name='choose_date'),
#     path('add_plan/', views.AddPlan.as_view(), name='add_plan'),
#     path('view_plans/', views.ViewPlans.as_view(), name='view_plans'),
#     path('edit_plan/<int:workout_plan_id>', views.EditPlan.as_view(),
#          name='edit_plan'),
#     path('delete_plan/<int:workout_plan_id>', views.DeletePlan.as_view(),
#          name='delete_plan'),
# ]
