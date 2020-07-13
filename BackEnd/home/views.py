from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.forms import UserCreationForm      
from django.contrib.auth.decorators import login_required

from .forms import About_form
# Create your views here.

def indexView(request):
    return render(request,'index.html')


@login_required  
def dashboardView(request):
    
    return render(request,'dashboard.html' )

def registerView(request):                         # to register new user with authentication
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = UserCreationForm()

    return render(request,'registration/register.html',{'form':form})

@login_required
def profile(request):
    form=About_form(request.POST or None , request.FILES or None) #create object of form

    if form.is_valid():
        form.save()

    return render(request,'registration/profile.html',{'form' : form})




