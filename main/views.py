from django.shortcuts import render

# Create your views here.

def home(request):
	return render(request,'index.html',{})


def blog(request):
	return render(request,'blog.html',{})


def career(request):
	return render(request,'career.html',{})


def services(request):
	return render(request,'services.html',{})
