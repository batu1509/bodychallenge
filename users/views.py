from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.mail import send_mail
import os

# Internal
from programs.models import Gender, LinearWorkout, Workout, WorkoutExercise, periodization
from users.models import ActivityLevel, Profile
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def userProfile(request, pk):
    """
    A view to display user profile
    """
    user = User.objects.get(username=pk)

    if request.user == user:
        gender = Profile.objects.filter(user=user).count
        ActivityLevel = Profile.objects.filter(user=user).first()
        bodyFat = Profile.objects.filter(user=user).last()

        context = {
            'user': user,
            'gender': Gender,
            'ActivityLevel': ActivityLevel,
            'bodyFat': bodyFat}
        return render(request, 'profile.html', context)

    else:
        messages.error(request,
                       "You don't have access to other user's details")
        return redirect('home')

