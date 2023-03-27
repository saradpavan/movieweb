from django.shortcuts import render, redirect
from django.http import HttpResponse
from saradpavanapp.models import moviefront
from django.contrib.auth.models import User, auth
from django.contrib import messages



def home(request):

    movie = moviefront.objects.all()

    return render(request,"index.html", {'movie':movie}) 

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invaild')
            return redirect('login')
        
    else:
        return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')


def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'already username taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'already email taken')
                return redirect('signup')
                
            else:
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save();
                print('user created')
                return redirect('login')

        else:
            messages.info(request,'password not matching')
            return redirect('signup')
        return redirect('/')
        
    else:
        return render(request,"signup.html")
     
    

def moviepage(request, id):
    if not request.user.is_authenticated:
        messages.info(request,"hey your not login,please login after use my website.")
        return redirect('login')
    movie = moviefront.objects.get(id=id)
    return render(request,"movie-page.html",{'movie': movie})
        
    
def playvideo(request,id):
    movie = moviefront.objects.get(id=id)

    return render(request,"playvideo.html", {'movie': movie})


    

def language(request):
    return render(request,"language.html")

def dubbed(request):
    return render(request,"dubbed.html")

def search(request):
    if request.method=="GET":
        query = request.GET['search'].lower()
        searching = moviefront.objects.filter(name=query)
    if searching.count()==0:
        messages.info(request,'no data found')
    
    return render(request,"search.html",{'searched':searching})
     

# Create your views here.
