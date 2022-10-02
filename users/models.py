from django.db import models
from django.contrib.auth.models import User
from programs.models import Gender
from PIL import Image


# Create your models here.

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profil')
    image = models.ImageField(null=True, blank=True, upload_to = 'profil_image/%Y/%m/')
    date_of_birth = models.DateField(null=True)
    # location_id = models.ForeignKey(Location, on_delete=models.RESTRICT, null=True)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, null=True)
    bio = models.CharField(max_length=180, null=True)
    # categories = models.ManyToManyField(Categorie, blank=False, related_name='categor')


    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        ## IMAGE RESIZE
        super().save(*args, **kwargs)
        if self.image:
            img = Image.open(self.image.path)
            if img.mode != 'RGB':
                img = img.convert('RGB')
            if img.height > 600 or img.width > 600:
                output_size = (600,600)
                img.thumbnail(output_size)
                img.save(self.image.path)