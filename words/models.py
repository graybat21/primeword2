import uuid

from django.db import models

# Create your models here.
from primeword_backend.settings import GRADE_CHOICE
from users.models import SchoolGroup, AcademyGroup


class Textbook(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    # grade = models.CharField(max_length=20)
    grade = models.CharField(max_length=2, choices=GRADE_CHOICE, blank=True)
    # user = models.ForeignKey('auth.User')
    school_code = models.ForeignKey(SchoolGroup, null=True)
    academy_code = models.ForeignKey(AcademyGroup, null=True)
    regdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    textbook = models.ForeignKey(Textbook)
    lesson = models.CharField(max_length=20)
    regdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.lesson


class Word(models.Model):
    spelling = models.CharField(max_length=100)
    memo = models.TextField(blank=True)
    note = models.ForeignKey(Note)
    meaning = models.CharField(max_length=500)
    regdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.spelling

# class Wordclass(models.Model):
#     classname = models.CharField(max_length=20)
#     memo = models.TextField(blank=True)
#
#     def __str__(self):
#         return str(self.classname)
#
#
# class Wordinfo(models.Model):
#     word = models.ForeignKey(Word)
#     wordclass = models.ForeignKey(Wordclass)
#     meaning = models.TextField(max_length=500)
#     symbol = models.CharField(max_length=50)
#
#     # regdate = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return str(self.word)
