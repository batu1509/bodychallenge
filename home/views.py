from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.mail import send_mail
import os

# Internal
from programs.models import Gender, LinearWorkout, Workout, WorkoutExercise, periodization
from users.models import ActivityLevel, Profile
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def home(request):

    return render(request, 'anasayfayazi.html')


def contact(request):

    if request.method == "POST":
        message = request.POST['message']

        if request.user.is_authenticated:
            message_name = request.user.username
            message_email = request.user.email

            if request.user.email:
                message_email = request.user.email
            else:
                message_email = request.POST['message-email']

        else:
            message_name = request.POST['message-name']
            message_email = request.POST['message-email']

        send_mail(
            'Message from ' + message_name +
            ' (' + message_email + ')',  
            message,  
            message_email,  
            [os.environ.get('EMAIL_HOST_USER')],  
        )

        context = {
            'message_name': message_name,
        }
        return render(request, 'contact.html', context)

    else:
        return render(request, 'contact.html', {})