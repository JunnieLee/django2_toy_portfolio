from django.shortcuts import render, get_object_or_404
from .models import Blog # (1)


# Create your views here.
def allblogs(request):
	blogposts = Blog.objects # (2) 
	# (1) + (2) = These will bring every Blog objects from the DB and change them into some usable python objects!
	return render(request, 'blog/allblogs.html', {'blogposts':blogposts})

def blogpostdetails(request, pk):
	post = get_object_or_404(Blog, pk=pk)
	return render(request, 'blog/blogpostdetails.html', {'post':post})