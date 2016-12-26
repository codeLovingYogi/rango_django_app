from django.http import HttpResponse
from django.shortcuts import render
from rango.models import Category, Page

def index(request):
	# Query database for a list of all categories currently stored
	# Order categories by number of likes in descending order
	# Retrieve top 5 only, or all if less than 5
	# Place list in context_dict dictionary which will be passed to template engine
	top_category_list = Category.objects.order_by('-likes')[:5]
	context_dict = {'categories': top_category_list}

	top_page_list = Page.objects.order_by('-views')[:5]
	context_dict['top_pages'] = top_page_list

	# Request a rendered request to send to the client
	# Making use of shortcut function to make our lives easier
	return render(request, 'rango/index.html', context_dict)

def about(request):
	return render(request, 'rango/about.html')

def category(request, category_name_slug):
	# Create context dictionary which we pass to template rendering engine
	context_dict = {}

	try:
		# Try to find category name slug with given name
		# If not found, .get() method raises a DoesNotExist exception
		# .get() method either returns one model instance or raises an exception
		category = Category.objects.get(slug=category_name_slug)
		context_dict['category_name'] = category.name

		# Retrieve all of associated pages
		pages = Page.objects.filter(category=category)

		# Adds result list to template context under name 'pages'
		context_dict['pages'] = pages

		# Add category object from database to context dictionary
		# Use this in template to verify that the category exists
		context_dict['category'] = category
	except:
		# If specified category not found, template displays 'no category' message
		pass

	return render(request, 'rango/category.html', context_dict)