from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	# Construct a dictionary to pass to the template engine as its context.
	context_dict = {'boldmessage': "I am bold front from the context"}

	# Request a rendered request to send to the client
	# Making use of shortcut function to make our lives easier
	return render(request, 'rango/index.html', context_dict)

def about(request):
	return HttpResponse("<h1>Rango says: Here is the About page.</h1> <a href='/rango/'>Index</a>")