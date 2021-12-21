from django.db import models


# Create your models here.

class Skill(models.Model):
    name = models.CharField(max_length=200)


class Candidate(models.Model):
    title = models.CharField(max_length=50)
    skills = models.ManyToManyField(Skill, through = 'CandidatesSkills', related_name='candidates')


class Job(models.Model):
    title = models.CharField(max_length=50)
    skills = models.ManyToManyField(Skill, through = 'JobsSkills', related_name='jobs')


class CandidatesSkills(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)


class JobsSkills(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
