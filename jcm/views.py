from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views import View
from jcm.models import Skill, Job
from jcm.models import Candidate
from jcm.forms import SkillForm, CandidateForm, JobForm


class JobView(View):
    def get(self, request):
        #skills_set = Skill.objects.all()
        job_set = Job.objects.all()

        context = {
            #"skills" : skills_set,
            "jobs": job_set
        }
        return render(request, 'jcm/templates/jobs.html', context)

    def post(self, request):
        form = JobForm(request.POST)
        new_job = form.save()
        return HttpResponseRedirect('/jcm/job')



class CandidateView(View):
    def get(self, request):
        #skills_set = Skill.objects.all()
        candidate_set = Candidate.objects.all()

        context = {
            #"skills" : skills_set,
            "candidates": candidate_set
        }
        return render(request, 'jcm/templates/candidates.html', context)

    def post(self, request):
        form = CandidateForm(request.POST)
        new_candidate = form.save()
        return HttpResponseRedirect('/jcm/candidate')


class SkillView(View):
    def get(self, request):
        skills_set = Skill.objects.all()
        context = {
            "skills": skills_set,
        }

        return render(request, 'jcm/templates/skills.html', context)

    def post(self, request):
        form = SkillForm(request.POST)
        new_skill = form.save()
        return HttpResponseRedirect('/jcm/skill')