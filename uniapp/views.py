from django.shortcuts import render, redirect
from django.http import HttpResponse
from uniproject.settings import RECAPTCHA_KEY
from .models import *
import requests
import json
from django.contrib import messages


def home(request):
    return render(request, 'index.html')

def qa_services(request):
    return render(request, 'qa-servies.html')

def web_dev(request):
    return render(request, 'web-dev.html')

def publishing(request):
    return render(request, 'publish-conversion.html')

def seo(request):
    return render(request, 'index.html')

def recruitment(request):
    return render(request, 'index.html')

def timecodes_translation(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about-us.html')

def save_contact_details(request):
    if request.method == 'POST':
        print(request.POST)
        name  = request.POST.get('fname')
        email  = request.POST.get('email')
        phone  = request.POST.get('phone')
        subject  = request.POST.get('subject')
        message  = request.POST.get('message')
        client_key = request.POST['g-recaptcha-response']
        secrate_key = RECAPTCHA_KEY
        captcha_data = {"secret":secrate_key,"response":client_key}
        r = requests.post("https://www.google.com/recaptcha/api/siteverify", data=captcha_data)
        
        response = json.loads(r.text)
        print('this is response:-',response)
        varify = response['success']
        print(message,subject,email,name,varify, sep='\n')
        
        if varify:
            ContactedUser.objects.create(name=name,email=email,phone=phone,subject=subject,message=message)
            messages.success(request, 'form submitted!!')
            return redirect('/')
        else:
            messages.warning(request, 'please try again!!')
    return redirect('/')


def save_newsletter_subscriber(request):
    if request.method == 'POST':
        try:
            print(request.POST)
            name  = request.POST.get('fname')
            email  = request.POST.get('email')
            NewsLetterSubscribers.objects.create(name=name,email=email)
            messages.success(request, 'subscribed!!')
            return redirect('/')
        except:
            messages.warning(request, 'please try again!!')
    return redirect('/')