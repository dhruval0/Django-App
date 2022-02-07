from datetime import datetime
import email
import re
from django.shortcuts import render, HttpResponse
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    # context = {
    #     'variable1':'dhruval',
    #     'variable2':'great'
    # }
    messages.success(request, "This is a text msg")
    return render(request, 'index.html')
    # return HttpResponse("This is my first Django application")

def about(request):
    return render(request,'about.html')
    # return HttpResponse("This is my about page")

def services(request):
    return render(request,'services.html')
    # return HttpResponse("I provide this kind of services")

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')

        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent')
    return render(request,'contact.html')
    # return HttpResponse("This is my contact")

def bio(request):
    return render(request, 'bio.html')