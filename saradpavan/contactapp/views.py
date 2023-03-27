from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.

from contactapp.models import Contact


def contact(request):
    if request.method == 'POST':
        contact = Contact(name=request.POST['name'],
        email=request.POST['email'],
        message=request.POST['message'])
        contact.save();
        return redirect('contact')
            
    else:
        return render(request,'contact.html')
