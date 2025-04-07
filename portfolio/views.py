from django.shortcuts import render

def home(request):
    return render(request, 'portfolio/index.html')

def resume(request):
    return render(request, 'portfolio/resume.html')

def contact(request):
    return render(request, 'portfolio/contact.html')

def projects(request):
    return render(request, 'portfolio/projects.html')
