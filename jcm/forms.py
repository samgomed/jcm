from django.forms import ModelForm
from jcm.models import Skill, Candidate, Job
from django import forms

class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = ['name']


class CandidatesForm(ModelForm):
    class Meta:
        model = Candidate
        fields = ['title']


class JobsForm(ModelForm):
    class Meta:
        model = Job
        fields = ['title']


class JobForm(forms.Form):
    skill_name = forms.SlugField()

class CandidateForm(forms.Form):
    skill_name = forms.SlugField()