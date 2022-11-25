from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.mail import send_mail
import os
from django.contrib.auth.decorators import login_required

# Internal
from programs.models import Gender, LinearWorkout, Workout, WorkoutExercise
from users.models import ActivityLevel, Profile
from .forms import UpdateUserForm, UpdateProfileForm

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



@login_required
def updateprofile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profil)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='updateprofile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profil)

    return render(request, 'updateprofile.html', {'user_form': user_form, 'profile_form': profile_form})