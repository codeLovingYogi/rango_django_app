from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

def index(request):
	# Request the context of the request
	# The context contains info such as the client's machine details, etc
	context = RequestContext(request)

	# Construct a dictionary to pass to the template engine as its context.
	context_dict = {'boldmessage': "I am bold front from the context"}

	# Request a rendered request to send to the client
	# Making use of shortcut function to make our lives easier
	return render_to_response('rango/index.html', context_dict, context)

def about(request):
	return HttpResponse("<h1>Rango says: Here is the About page.</h1> <a href='/rango/'>Index</a>")