from django.db import models


# Create your models here.

class Skill(models.Model):
    name = models.CharField(max_length=200)


class Book(models.Model):
    title = models.CharField(max_length=50)
    skill = models.ForeignKey('Skill', on_delete=models.SET_NULL, null=True)


class Job(models.Model):
    title = models.CharField(max_length=50)
    skill = models.ForeignKey('Skill', on_delete=models.SET_NULL, null=True)
