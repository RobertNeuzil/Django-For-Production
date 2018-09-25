from django.shortcuts import render
from .models import Blog_Post




def index(request):

	
	posts = Blog_Post.objects.order_by('id')


	
	context = {'posts': posts}
	return render(request, 'home/index.html', context)

def about(request):
	return render(request, 'home/about.html')

