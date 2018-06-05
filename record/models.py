from django.db import models

# Create your models here.
from users.models import Profile
from words.models import Note


class StudyRecord(models.Model):
    user = models.ForeignKey(Profile)
    note = models.ForeignKey(Note)
    step = models.CharField(max_length=2, default='1')
    unknownwords = models.TextField(default='')
    regdate = models.DateTimeField(auto_now_add=True)
    # def __str__(self):
    #     return self.lesson


class TestRecord(models.Model):
    user = models.ForeignKey(Profile)
    note = models.ForeignKey(Note)
    score = models.CharField(max_length=5, default='0')
    regdate = models.DateTimeField(auto_now_add=True)