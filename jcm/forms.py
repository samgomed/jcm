from django.forms import ModelForm
from jcm.models import Skill, Candidate, Job


class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = ['name']


class CandidateForm(ModelForm):
    class Meta:
        model = Candidate
        fields = ['title']


class JobForm(ModelForm):
    class Meta:
        model = Job
        fields = ['title']