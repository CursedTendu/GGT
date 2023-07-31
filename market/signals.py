from authentication.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile, Rating
from django.db.models import Avg

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=Rating)
def update_average_rating(sender, instance, **kwargs):
    user = instance.user
    ratings = Rating.objects.filter(user=user)
    average_rating = ratings.aggregate(Avg('rating'))['rating__avg']
    profile = Profile.objects.get(user=user)
    profile.average_rating = average_rating
    profile.save()