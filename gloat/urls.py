"""gloat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
import jcm.views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jcm/', TemplateView.as_view(template_name='jcm/templates/main.html')),
    path('jcm/skill/', jcm.views.SkillView.as_view()),
    path('jcm/candidate/', jcm.views.CandidateView.as_view()),
    path('jcm/job/', jcm.views.JobView.as_view()),
    path('jcm/job/<slug:id>/candidates', jcm.views.CandidateFinderView.as_view()),
]

urlpatterns += staticfiles_urlpatterns()