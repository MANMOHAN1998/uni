from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'index.html')

def qa_services(request):
    return render(request, 'index.html')

def web_dev(request):
    return render(request, 'index.html')

def publishing(request):
    return render(request, 'index.html')

def seo(request):
    return render(request, 'index.html')

def recruitment(request):
    return render(request, 'index.html')

def timecodes_translation(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about-us.html')

def contact(request):
    return render(request, 'contact.html')