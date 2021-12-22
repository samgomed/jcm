from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views import View
from jcm.models import Skill, Job
from jcm.models import Candidate, CandidatesSkills,JobsSkills
from jcm.forms import SkillForm, CandidateForm, JobForm, JobsForm, CandidatesForm


class CandidateFinderView(View):
    def get(self, request, id):
        job_id = int(id)
        job = Job.objects.get(pk=job_id)
        candidates_ids = self.candidate_finder(job)
        context = {
            'job_id' : job_id,
            'job_name': job.title,
            'candidates_ids' : candidates_ids
        }
        return render(request, 'jcm/templates/match.html', context)


    def candidate_finder(self, job):
        job_skills = [skill['name'] for skill in job.skills.values()]

        job_candidates = Candidate.objects.filter(title=job.title).values()

        if len(job_skills) == 0:
            return [candidate['id'] for candidate in job_candidates]

        max_intersection = 0
        candidates = []
        for candidate in job_candidates:
            candidate_id = candidate['id']
            candidate_skills = [skill['name'] for skill in Candidate.objects.get(pk = candidate_id).skills.values()]
            intersection = set(candidate_skills).intersection(job_skills)
            if (len(intersection) < max_intersection):
                continue
            if len(intersection) > max_intersection:
                candidates.clear()
                max_intersection = len(intersection)
            candidates.append(candidate_id)

        return candidates



class JobsView(View):
    def get(self, request):
        job_set = Job.objects.all()
        context = {
            "jobs": job_set
        }
        return render(request, 'jcm/templates/jobs.html', context)

    def post(self, request):
        form = JobsForm(request.POST)
        new_job = form.save()
        return HttpResponseRedirect('/jcm/job')

class JobView(View):
    def get(self, request, id):
        job = Job.objects.get(pk=int(id))
        job_skills = [skill['name'] for skill in job.skills.values()]
        context = {
            "job_id": id,
            "job_title": job.title,
            "job_skills": job_skills,
            "form" : JobForm()
        }
        return render(request, 'jcm/templates/job.html', context)

    def post(self, request, id):
        skill_name = request.POST['skill_name']
        job_skill = Skill.objects.get(name = skill_name)
        job_object = Job.objects.get(pk = int(id))
        js = JobsSkills(skill = job_skill, job = job_object)
        js.save()
        return HttpResponseRedirect('/jcm/job/'+ id)

class CandidatesView(View):
    def get(self, request):
        candidate_set = Candidate.objects.all()

        context = {
            "candidates": candidate_set
        }
        return render(request, 'jcm/templates/candidates.html', context)

    def post(self, request):
        form = CandidatesForm(request.POST)
        new_candidate = form.save()
        return HttpResponseRedirect('/jcm/candidate')

class CandidateView(View):
    def get(self, request, id):
        candidate = Candidate.objects.get(pk=int(id))
        candidate_skills = [skill['name'] for skill in candidate.skills.values()]
        context = {
            "candidate_id": id,
            "candidate_title": candidate.title,
            "candidate_skills": candidate_skills,
            "form" : CandidateForm()
        }
        return render(request, 'jcm/templates/candidate.html', context)

    def post(self, request, id):
        skill_name = request.POST['skill_name']
        candidate_skill = Skill.objects.get(name = skill_name)
        candidate_object = Candidate.objects.get(pk = int(id))
        js = CandidatesSkills(skill = candidate_skill, candidate = candidate_object)
        js.save()
        return HttpResponseRedirect('/jcm/candidate/'+ id)

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