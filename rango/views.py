from django.http import HttpResponse
from django.shortcuts import render
from rango.models import Category

def index(request):
	# Query database for a list of all categories currently stored
	# Order categories by number of likes in descending order
	# Retrieve top 5 only, or all if less than 5
	# Place list in context_dict dictionary which will be passed to template engine
	category_list = Category.objects.order_by('-likes')[:5]
	context_dict = {'categories': category_list}

	# Request a rendered request to send to the client
	# Making use of shortcut function to make our lives easier
	return render(request, 'rango/index.html', context_dict)

def about(request):
	return render(request, 'rango/about.html')