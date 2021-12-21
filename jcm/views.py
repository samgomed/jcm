from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from jcm.models import Skill


class SkillView(View):
    def get(self, request):
        skills_set = Skill.objects.all()
        context = {
            "skills": skills_set,
        }

        return render(request, 'jcm/templates/skills.html', context)
