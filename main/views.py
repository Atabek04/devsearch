from multiprocessing import context
from django.shortcuts import render

projectList = [
	{
		'id' : '1',
		'title' : 'Social Network',
		'description' : 'A website for online meets',
		'topRated': True,
	},
	{
		'id' : '2',
		'title' : 'Snake game',
		'description' : 'A game with snakes',
		'topRated' : False,
	},
	{
		'id' : '3',
		'title' : 'EShop',
		'description' : 'Online shop platform',
		'topRated' : True,
	}
]


def index(request):
	return render(request, 'main/index.html')

def contact(request):
	# name = 'Otabek'
	# age = 18

	context = {
		'projects' : projectList
	}
	return render(request, 'main/contact.html', context)

def project(request, pk):
	projectObject = None

	for i in projectList:
		if i['id'] == str(pk):
			projectObject = i
	context = {
		'project' : projectObject
	}
	return render(request, 'main/project.html', context)