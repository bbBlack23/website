from django.shortcuts import render,redirect, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages 

# Create your views here.

def index(request):
    context = {
        'variable':"this is sent"
    }
    return render(request, 'index.html', context)
    # return HttpResponse("This is Home")

def about(request):
    return render(request, 'about.html')

    # return HttpResponse("This is About")

def services(request):
    return render(request, 'services.html')

    # return HttpResponse("This is Services")

def contact(request):
    if request.method== "POST":
        name = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact = Contact(name=name,email=email,phone=phone,message=message,date=datetime.today())
        contact.save()
        messages.success(request, 'Your Message is Sent!')
    return render(request, 'contact.html')

    # return HttpResponse("This is Contact")