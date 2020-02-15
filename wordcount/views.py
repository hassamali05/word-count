from django.http import HttpResponse
from django.shortcuts import render
def home(request):
	return render(request,'home.html',{'name':'Hassam'})

def count(request):
	fulltext = request.GET['fulltext']
	lst = fulltext.split()
	return render(request,'count.html',{'count':len(lst),'fulltext':fulltext})

def about(request):
	return render(request,'about.html')