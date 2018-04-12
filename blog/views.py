from django.shortcuts import render
from .models import Blog # (1)

# Create your views here.
def allblogs(request):
	blogposts = Blog.objects # (2) 
	# (1) + (2) = These will bring every Blog objects from the DB and change them into some usable python objects!
	return render(request, 'blog/allblogs.html', {'blogposts':blogposts})