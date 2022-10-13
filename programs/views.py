from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from programs.models import Muscle, MuscleGroup, Level, Routine, RoutineGoal, RoutineType, Equipment, Exercise, ExerciseMechanic, ExerciseType, Workout, WorkoutExercise, WorkoutExerciseSet, WorkoutExerciseSetWithReps, Gender, periodization, LinearWorkout, CircularWorkout, repType, IntervalWorkoutExerciseSet
from programs.serializers import MuscleSerializer, MuscleGroupSerializer, LevelSerializer, RoutineGoalSerializer, RoutineSerializer, RoutineTypeSerializer, EquipmentSerializer, ExerciseSerializer, ExerciseMechanicSerializer, ExerciseTypeSerializer, WorkoutExerciseSerializer, WorkoutExerciseSetSerializer, WorkoutExerciseSetWithRepsSerializer, LinearWorkoutSerializer, CircularWorkoutSerializer, GenderSerializer, repTypeSerializer, WorkoutSerializer, periodizationSerializer, IntervalWorkoutExerciseSetSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from programs.permissions import KendiProfilYaDaReadOnly, IsAdminUserOrReadOnly
from rest_framework.filters import SearchFilter
from users.models import Profile, ActivityLevel, BodyWeight, BodyHeight, MeasurementUnit, MeasurementParameter, SavedRoutine, BodyVitalsLog
from users.serializers import ProfileImageSerializer, ProfileSerializer, ActivityLevelSerializer, BodyWeightSerializer, BodyHeightSerializer, MeasurementParameterSerializer, MeasurementUnitSerializer, SavedRoutineSerializer, BodyVitalsLogSerializer

class BodyVitalsLogViewSet(ModelViewSet):
    queryset = BodyVitalsLog.objects.all()
    serializer_class = BodyVitalsLogSerializer
    permission_classes = [IsAuthenticated]

class SavedRoutineViewSet(ModelViewSet):
    queryset = SavedRoutine.objects.all()
    serializer_class = SavedRoutineSerializer
    permission_classes = [IsAuthenticated]

class MeasurementParameterViewSet(ModelViewSet):
    queryset = MeasurementParameter.objects.all()
    serializer_class = MeasurementParameterSerializer
    permission_classes = [IsAuthenticated]

class MeasurementUnitViewSet(ModelViewSet):
    queryset = MeasurementUnit.objects.all()
    serializer_class = MeasurementUnitSerializer
    permission_classes = [IsAuthenticated]

class ActivityLevelViewSet(ModelViewSet):
    queryset = ActivityLevel.objects.all()
    serializer_class = ActivityLevelSerializer
    permission_classes = [IsAuthenticated]

class WeightLevelViewSet(ModelViewSet):
    queryset = BodyWeight.objects.all()
    serializer_class = BodyWeightSerializer
    permission_classes = [IsAuthenticated]

class HeightLevelViewSet(ModelViewSet):
    queryset = BodyHeight.objects.all()
    serializer_class = BodyHeightSerializer
    permission_classes = [IsAuthenticated]

class ProfilViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [KendiProfilYaDaReadOnly]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)

class ProfilImageUpdateView(generics.UpdateAPIView):
    serializer_class = ProfileImageSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        profil_image = self.request.user.profil
        return profil_image

class MuscleViewSet(ModelViewSet):
    queryset = Muscle.objects.all()
    serializer_class = MuscleSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    filter_backends = [SearchFilter]
    search_fields = ['name']

class MuscleGroupViewSet(ModelViewSet):
    queryset = MuscleGroup.objects.all()
    serializer_class = MuscleGroupSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class EquipmentViewSet(ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class LevelViewSet(ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class RoutineGoalViewSet(ModelViewSet):
    queryset = RoutineGoal.objects.all()
    serializer_class = RoutineGoalSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class RoutineTypeViewSet(ModelViewSet):
    queryset = RoutineType.objects.all()
    serializer_class = RoutineTypeSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class ExerciseMechanicViewSet(ModelViewSet):
    queryset = ExerciseMechanic.objects.all()
    serializer_class = ExerciseMechanicSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class ExerciseTypeViewSet(ModelViewSet):
    queryset = ExerciseType.objects.all()
    serializer_class = ExerciseTypeSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class WorkoutExerciseViewSet(ModelViewSet):
    queryset = WorkoutExercise.objects.all()
    serializer_class = WorkoutExerciseSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class WorkoutExerciseSetViewSet(ModelViewSet):
    queryset = WorkoutExerciseSet.objects.all()
    serializer_class = WorkoutExerciseSetSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class WorkoutExerciseSetWithRepsViewSet(ModelViewSet):
    queryset = WorkoutExerciseSetWithReps.objects.all()
    serializer_class = WorkoutExerciseSetWithRepsSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class GenderViewSet(ModelViewSet):
    queryset = Gender.objects.all()
    serializer_class = GenderSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class periodizationViewSet(ModelViewSet):
    queryset = periodization.objects.all()
    serializer_class = periodizationSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class CircularWorkoutViewSet(ModelViewSet):
    queryset = CircularWorkout.objects.all()
    serializer_class = CircularWorkoutSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class LinearWorkoutViewSet(ModelViewSet):
    queryset = LinearWorkout.objects.all()
    serializer_class = LinearWorkoutSerializer
    permission_classes = [IsAdminUserOrReadOnly]    

class IntervalWorkoutExerciseSetViewSet(ModelViewSet):
    queryset = IntervalWorkoutExerciseSet.objects.all()
    serializer_class = IntervalWorkoutExerciseSetSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class repTypeViewSet(ModelViewSet):
    queryset = repType.objects.all()
    serializer_class = repTypeSerializer
    permission_classes = [IsAdminUserOrReadOnly] 
    

class RoutineViewSet(ModelViewSet):
    queryset = Routine.objects.all()
    serializer_class = RoutineSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    filter_backends = [SearchFilter]
    search_fields = ['name']

class ExerciseViewSet(ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permission_classes = [KendiProfilYaDaReadOnly]
    filter_backends = [SearchFilter]
    search_fields = ['name']

class WorkoutViewSet(ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    permission_classes = [KendiProfilYaDaReadOnly]
    filter_backends = [SearchFilter]
    search_fields = ['name']




    # def perform_create(self, serializer):
    #     location_name = self.request
    #     serializer.save(location_name=location_name)





# class CategoriViewSet(ModelViewSet):
#     queryset = Categorie.objects.all()
#     serializer_class = CategoriSerializer
#     permission_classes = [IsAuthenticated, IsAdminUserOrReadOnly]


















# class ProfilViewSet(
#                 mixins.ListModelMixin,
#                 mixins.RetrieveModelMixin,
#                 mixins.UpdateModelMixin,
#                 GenericViewSet):

#     queryset = Profile.objects.all()
#     serializer_class = ProfilSerializer
#     permission_classes = [IsAuthenticated, KendiProfilYaDaReadOnly]


    # def get_queryset(self):
    #     if self.action == 'list':
    #         return self.queryset.filter(user=self.request.user)
    #     return self.queryset