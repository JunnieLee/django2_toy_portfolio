from django.shortcuts import render
from .models import Job # (1)

# Create your views here.
def home(request):
	jobs = Job.objects # (2) 
	# (1) + (2) = These will bring every Job objects from the DB and change them into some usable python objects!
	return render(request, 'jobs/home.html', {'jobs':jobs})