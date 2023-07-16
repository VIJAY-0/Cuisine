from django.shortcuts import render
from django.http import HttpResponseRedirect ,HttpResponse
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login ,logout

# from django.contrib.auth 





def signup(request):
    if request.method =="POST":
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        if pass1!=pass2:
            messages.warning(request,extra_tags='signup',message= "Passwords Not matching")
            return render(request,'Accounts/signup.html')
        try:

            if User.objects.get(username=email) :
                messages.warning(request,extra_tags='signup',message= "User name already taken")
                return render(request,'Accounts/signup.html')
        except Exception as id:
            pass

        user=User.objects.create_user(email=email,username=email,password=pass1)
        user.is_active=True
        user.save()
        # messages.warning(request,extra_tags='signup',message= "Created user  -- " + email)
        # messages.warning(request,extra_tags='signup',message= "Created user  -- " + email)
        return HttpResponseRedirect(reverse('Accounts:login'))
    else:    
        return render(request,'Accounts/signup.html')


def login_(request):
    if request.method =="POST":
        email=request.POST['username']
        passw=request.POST['pass1']

        user=authenticate(username=email,password=passw)
        if user is not None:
            login(request,user)
            # messages.warning(request,extra_tags='login',message= "Logged in ")
            return HttpResponseRedirect(reverse('Home:home'))
        else:
            messages.warning(request,extra_tags='login',message= "Invalid Credentials")
            return HttpResponseRedirect(reverse('Accounts:login'))

    return render(request,'Accounts/login.html')

def logout_(request):
    logout(request)
    return HttpResponseRedirect(reverse('Home:home'))