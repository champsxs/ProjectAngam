from django.db.models.signals import post_save, post_delete
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.shortcuts import render

from .models import Profile

@receiver(post_save, sender=User)
def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        user_profile = Profile.objects.create(
            user = user,
            username = user.username,
            email = user.email,
            name = user.first_name,
        )
        subject = "Your account succesully created"
        message = "Welcome to my test project"
        
        # send_mail(
        #     subject,
        #     message,
        #     settings.EMAIL_HOST_USER,
        #     [user_profile.email],
        #     fail_silently=False,
        # )

        
@receiver(post_save, sender=Profile)
def updateUser(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user
    if not created:
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()

        subject = "Your account succesully created"
        message = "Welcome to my test project"
        print("sending email.............")
        send_mail(
            subject,
            message,
            'sxshit@localhost',
            [user.email],
            fail_silently=False,
        )



@receiver(post_delete, sender=Profile)
def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()


# post_save.connect(createProfile, sender=Profile)
# post_delete.connect(deleteUser, sender=Profile)