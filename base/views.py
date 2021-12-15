from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
	return render(request, 'base/index.html')

def posts(request):

	posts = [
		{
			'headline': 'Headline # 1',
			'sub_headline': 'Some random words to take up this space please.',
		},
		{
			'headline': 'Headline # 2',
			'sub_headline': 'More random words for the space taking up.',
		},
		{
			'headline': 'Headline #3',
			'sub_headline': 'Uggggggggggggggghhhhhhhhhhhhhhhhhhhh',
		},
	]
	context = {'posts': posts}
	return render(request, 'base/posts.html', context)

def post(request):
	return render(request, 'base/post.html')

def profile(request):
	return render(request, 'base/profile.html')