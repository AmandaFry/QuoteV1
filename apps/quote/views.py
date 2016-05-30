from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Category, Quote

def index(request):

 	try:#make the assumption session exists first 
 		if (request.session['count'] < 22):
			request.session['count'] = request.session['count'] + 1
		else:
			request.session['count'] = 1
	except:#this will only happens one, if you don't have this the first time the page will not render
		request.session['count'] = 1

	secondq = Quote.objects.get(id=request.session['count'])

 	context = {
 		"quote" : secondq,
 	}
	return render(request, 'quote/index.html', context)

def showOne(request):
	print ("*" *20)
	print 'I am inside the redirect'
	print ("*" *20)
	return render(request, 'quote/showOne.html')

def clear(request):
	del request.session['count']
	return redirect('/')