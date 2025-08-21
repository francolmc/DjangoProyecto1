from django.shortcuts import render
from .models import Projects, PROJECTS_DATA

# Create your views here.
def portafolio_home(request):
    projects_not_draft = []
    for project in PROJECTS_DATA:
        if not project.is_draft():
            projects_not_draft.append(project)
    #
    # projects_not_draft = [
    #     a for a in PROJECTS_DATA if not a.is_draft()
    # ]
    #

    return render(request, 'portafolio_home.html', { 'projects': projects_not_draft })