from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views import View
from jcm.models import Skill
from jcm.models import Candidate
from jcm.forms import SkillForm

class CandidateView(View):
    def get(self, request):
        skills_set = Skill.objects.all()
        candidate_set = Candidate.objects.all()

        context = {
            "skills" : skills_set,
            "candidates" : candidate_set
        }
        return render(request, 'jcm/templates/candidates.html', context)

    def post(self, request):
        pass

class SkillView(View):
    def get(self, request):
        skills_set = Skill.objects.all()
        context = {
            "skills": skills_set,
        }

        return render(request, 'jcm/templates/skills.html', context)

    def post(self, request):
        '''
        form = SkillForm(request.POST)

        if form.is_valid():
            skill_name = form.cleaned_data['skill_name']

            s = Skill(name=skill_name)
            s.save()

            return HttpResponseRedirect('/skill')
        '''
        form = SkillForm(request.POST)
        new_skill = form.save()
        return HttpResponseRedirect('/jcm/skill')