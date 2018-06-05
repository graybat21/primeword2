from django.contrib.auth.models import User
from django.db import models
# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver

from primeword_backend.settings import GRADE_CHOICE


class SchoolGroup(models.Model):
    code = models.CharField(max_length=5, primary_key=True)
    name = models.CharField(max_length=10)

    def __str__(self):
        return str(self.name)


class AcademyGroup(models.Model):
    code = models.CharField(max_length=5, primary_key=True)
    name = models.CharField(max_length=10)

    def __str__(self):
        return str(self.name)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    grade = models.CharField(max_length=2, choices=GRADE_CHOICE, blank=True)
    school_code = models.ForeignKey(SchoolGroup, null=True)
    academy_code = models.ForeignKey(AcademyGroup, null=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
