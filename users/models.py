from tokenize import blank_re
from django.db import models
from django.contrib.auth.models import User
from django.forms import IntegerField
from programs.models import Gender, Routine
from PIL import Image
from django.utils.translation import gettext_lazy as _


# Create your models here.
class BodyHeight(models.Model):
    height = models.IntegerField(blank=True, null=True)

class BodyWeight(models.Model):
    weight = models.FloatField(blank=True, null=True)

class MeasurementParameter(models.Model):
    parameter = models.CharField(max_length=255, null=True)

class MeasurementUnit(models.Model):
    unit = models.CharField(max_length=255, null=True)
    parameter = models.ForeignKey(MeasurementParameter, on_delete=models.CASCADE, null=True)

class ActivityLevel(models.Model):
    level = models.CharField(_('level'), max_length=255, null=True)
    description = models.CharField(max_length=255, null=True)

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profil')
    profilePhoto = models.ImageField(null=True, blank=True, upload_to = 'profil_image/%Y/%m/')
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, null=True)
    bio = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(null=True)
    bodyFat = models.FloatField(blank=True, null=True)
    activityLevel = models.ForeignKey(ActivityLevel, on_delete=models.CASCADE, null=True)
    createDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        ## IMAGE RESIZE
        super().save(*args, **kwargs)
        if self.profilePhoto:
            img = Image.open(self.profilePhoto.path)
            if img.mode != 'RGB':
                img = img.convert('RGB')
            if img.height > 600 or img.width > 600:
                output_size = (600,600)
                img.thumbnail(output_size)
                img.save(self.profilePhoto.path)


class BodyVitalsLog(models.Model):
    profileId = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    createDate = models.DateTimeField(auto_now_add=True)
    activityLevel = models.ForeignKey(ActivityLevel, on_delete=models.CASCADE, null=True)
    height = models.ForeignKey(BodyHeight, on_delete=models.CASCADE, null=True)
    weight = models.ForeignKey(BodyWeight, on_delete=models.CASCADE, null=True)
    

class SavedRoutine(models.Model):
    saverId = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    routineId = models.ForeignKey(Routine, on_delete=models.CASCADE, null=True)
    saveData = models.DateTimeField(auto_now_add=True)