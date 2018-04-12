from django.shortcuts import render, get_object_or_404
from .models import Job # (1)

# Create your views here.
def home(request):
	jobs = Job.objects # (2) 
	# (1) + (2) = These will bring every Job objects from the DB and change them into some usable python objects!
	return render(request, 'jobs/home.html', {'jobs':jobs})

def jobs_detail(request, pk):
	job_post = get_object_or_404(Job, pk=pk)
	return render(request, 'jobs/jobs_detail.html', {'job_post':job_post})