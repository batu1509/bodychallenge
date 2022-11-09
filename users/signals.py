from django.contrib.auth.models import User
from users.models import Profile
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_profil(sender, instance, created, **kwargs):
    print(instance.username, '___Created: ', created)
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profil.save()











# @receiver(post_save, sender=Profile)
# def create_ilk_durum_mesaji(sender, instance, created, **kwargs):
#     if created:
#         ProfilDurum.objects.create(
#             user_profil=instance,
#             durum_mesaji= f'{instance.user.username} kulübe katıldı.'
#         )