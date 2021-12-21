from django import forms
from django.forms import ModelForm
from jcm.models import Skill
'''
class SkillForm(forms.Form):
    skill_name = forms.CharField(label='Skill name', max_length=100)
'''

class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = ['name']